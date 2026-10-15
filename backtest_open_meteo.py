#!/usr/bin/env python3
"""
Red Devil Bison Farm — Forecast Backtest (Open-Meteo Previous Runs)

Looks BACKWARD: for every day KMDPOOLE58 has a settled daily summary, asks
Open-Meteo what each weather model had predicted 1, 2 ... 7 days earlier, turns
that into a daily high, low and rain total, and writes backtest_log.csv in the
same layout forecast_log.csv uses. score_forecasts.py then scores it:

    python backtest_open_meteo.py
    python score_forecasts.py backtest_log.csv backtest_scores.csv backtest_scores.md

Source: Open-Meteo Previous Runs API (previous-runs-api.open-meteo.com), which
stores, for each hour, the value a model forecast N x 24 hours before it.

Rules (same as the rest of the repo)
  - Nothing is estimated. A day is used only when ALL 24 hours are present for
    that lead time; otherwise that day/lead/model is skipped, not filled in.
  - Dates are Eastern. Lead 1 = made about 24 h ahead ... lead 7 = about 168 h.
    Lead 0 (the newest run) is deliberately not used; it already contains
    recent observations and would flatter every model.
  - Daily high/low come from HOURLY values, so a model's high can sit a little
    under the station's true peak. Compare models with each other first.
  - A model name Open-Meteo rejects is skipped and listed on the run summary,
    with the reason Open-Meteo gave. The model list below is the one place to
    edit.
  - start_date/end_date are used as given. A failed request is retried with the
    same dates; there is no past_days fallback, because past_days tops out at
    92 and would quietly drop the oldest station days.
"""

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import forecast_log as fl  # reuse fetch_json, FIELDS, LAT/LON

TZ = ZoneInfo("America/New_York")
HISTORY_FILE = "weather_history.csv"
OUT_FILE = "backtest_log.csv"
API = "https://previous-runs-api.open-meteo.com/v1/forecast"
LEADS = range(1, 8)

# (label used in the scorecard, value for Open-Meteo's models= parameter or None)
# No "best match" entry: at the farm the API's default returned exactly the
# gfs_seamless values on all 714 day-leads of the first backtest (2026-10-14),
# so it would only score GFS twice.
MODELS = [
    ("om-ecmwf-ifs", "ecmwf_ifs025"),
    ("om-ecmwf-hres", "ecmwf_ifs"),
    ("om-gfs", "gfs_seamless"),
    ("om-nbm", "ncep_nbm_conus"),
    ("om-icon", "icon_seamless"),
    ("om-gem", "gem_seamless"),
]


def truth_dates(path=HISTORY_FILE):
    days = set()
    if Path(path).exists():
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                d = (r.get("yest_date") or "").strip()
                if d:
                    days.add(d)
    return days


def build_url(model, start, end):
    hourly = []
    for n in LEADS:
        hourly += [f"temperature_2m_previous_day{n}", f"precipitation_previous_day{n}"]
    q = {
        "latitude": fl.LAT, "longitude": fl.LON, "hourly": ",".join(hourly),
        "temperature_unit": "fahrenheit", "precipitation_unit": "inch",
        "timezone": "America/New_York",
    }
    q["start_date"], q["end_date"] = start, end
    if model:
        q["models"] = model
    return API + "?" + urllib.parse.urlencode(q)


def get_series(hourly, var, lead):
    key = f"{var}_previous_day{lead}"
    if key in hourly:
        return hourly[key]
    alt = next((k for k in hourly if k.startswith(key + "_")), None)  # model-suffixed
    return hourly[alt] if alt else None


def daily_rows(label, data, targets):
    """One row per (target day, lead) for which all 24 hours exist."""
    hourly = (data or {}).get("hourly") or {}
    times = hourly.get("time") or []
    by_day = {}
    for i, t in enumerate(times):
        by_day.setdefault(str(t)[:10], []).append(i)

    rows = []
    for lead in LEADS:
        temp = get_series(hourly, "temperature_2m", lead)
        rain = get_series(hourly, "precipitation", lead)
        if temp is None:
            continue
        for day, idxs in sorted(by_day.items()):
            if day not in targets or len(idxs) != 24:
                continue
            t24 = [temp[i] for i in idxs]
            if any(v is None for v in t24):
                continue
            r24 = [rain[i] for i in idxs] if rain is not None else None
            precip = round(sum(r24), 2) if r24 and all(v is not None for v in r24) else ""
            log_date = date.fromisoformat(day) - timedelta(days=lead)
            logged = datetime(log_date.year, log_date.month, log_date.day, 9, 0, tzinfo=TZ)
            rows.append({
                "log_date": log_date.isoformat(),
                "logged_et": logged.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "source": label, "target_date": day, "lead_days": lead,
                "high_f": round(max(t24), 2), "low_f": round(min(t24), 2),
                "precip_prob_pct": "", "precip_in": precip,
            })
    return rows


def main():
    targets = truth_dates()
    if not targets:
        print("No station days found in weather_history.csv (yest_date column).")
        sys.exit(1)
    start, end = min(targets), max(targets)
    print(f"Backtest window {start} to {end} ({len(targets)} station days)")

    all_rows, report = [], []
    for label, model in MODELS:
        # Three tries, 20 s apart: Open-Meteo's free tier times out or
        # rate-limits now and then, and a retry usually gets through.
        data, seen = None, len(fl.errors)
        for attempt in range(3):
            if attempt:
                time.sleep(20)
            data = fl.fetch_json(build_url(model, start, end))
            if data is not None:
                break
        fl.errors[seen:] = [f"{label}: {e}" for e in fl.errors[seen:]]
        rows = daily_rows(label, data, targets)
        all_rows += rows
        leads = sorted({r["lead_days"] for r in rows})
        report.append((label, model or "default", len(rows), leads))

    with open(OUT_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fl.FIELDS)
        w.writeheader()
        w.writerows(all_rows)

    for label, model, n, leads in report:
        print(f"  {label:16s} models={model:16s} {n} day-leads, leads {leads}" if n else
              f"  {label:16s} models={model:16s} NO DATA (see the notes below for why)")
    for e in fl.errors:
        print(f"  note: {e}")
    if not all_rows:
        print("Nothing retrieved.")
        sys.exit(1)


if __name__ == "__main__":
    main()
