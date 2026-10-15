#!/usr/bin/env python3
"""
Red Devil Bison Farm — Forecast Logger

Saves what the forecasters predicted, so the predictions can later be scored
against what KMDPOOLE58 actually recorded (see score_forecasts.py).

Why this exists: nobody keeps a free archive of yesterday's forecasts. The only
way to know how good a forecast was 7 days ahead is to write it down 7 days
ahead. Every run appends one row per source per target day:

    log_date, logged_et, source, target_date, lead_days,
    high_f, low_f, precip_prob_pct, precip_in

Sources
  open-meteo-ecmwf   ECMWF IFS model alone, out to 15 days ahead
  open-meteo-gfs     NOAA GFS model alone, out to 15 days ahead
  nws                National Weather Service, ~7 days ahead

  No Open-Meteo default ("best match") source: at the farm it returned exactly
  the GFS values (all 16 days on 2026-10-14, and all 714 day-leads of the
  backtest), so it would only score GFS twice.

Data-integrity rules (same as fetch_weather.py)
  - Nothing is estimated. A value a source did not give is left blank.
  - All dates are Eastern. lead_days = target_date - log_date (0 = same day).
  - One row per (log_date, source, target_date). Re-running the same day never
    overwrites the first forecast saved that day, so lead times stay honest.

NWS notes
  - NWS publishes 12-hour periods. A day's HIGH is its daytime period. A day's
    LOW is the night period that starts the evening before (or the overnight
    period that starts after midnight), because the calendar-day low normally
    happens before dawn. Today's low is blank once the night is already over.
  - NWS sometimes returns no rain chance when it means 0%. That is left blank,
    not turned into 0.
"""

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

LAT, LON = 39.151, -77.462  # Poolesville, MD (same as fetch_weather.py)
TZ = ZoneInfo("America/New_York")
LOG_FILE = "forecast_log.csv"
USER_AGENT = "RDBF-forecast-logger (github.com/rdbfarm)"
MAX_LEAD = 15

FIELDS = [
    "log_date", "logged_et", "source", "target_date", "lead_days",
    "high_f", "low_f", "precip_prob_pct", "precip_in",
]

errors = []  # human-readable list of anything that failed


def fetch_json(url, headers=None, timeout=30):
    """GET a URL, return parsed JSON or None (never raises). Never logs the query string."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        # Open-Meteo says WHY in the body of a 400 or 429 (a model name it does
        # not know, a rate limit); keep that, or "no data" hides the cause.
        reason = ""
        if isinstance(e, urllib.error.HTTPError):
            try:
                reason = json.loads(e.read().decode("utf-8")).get("reason") or ""
            except Exception:
                pass
        errors.append(f"{url.split('?')[0]} -> {type(e).__name__}: {e}"
                      + (f" ({reason})" if reason else ""))
        return None


def num(v):
    """Float or None. Blank, null and NaN all become None."""
    try:
        if v is None or v == "":
            return None
        f = float(v)
        return None if f != f else f
    except (TypeError, ValueError):
        return None


# ── Open-Meteo ───────────────────────────────────────────────────────────────
OM_DAILY = [
    "temperature_2m_max", "temperature_2m_min",
    "precipitation_probability_max", "precipitation_sum",
]


def open_meteo_url(model=None):
    q = {
        "latitude": LAT, "longitude": LON,
        "daily": ",".join(OM_DAILY),
        "temperature_unit": "fahrenheit", "precipitation_unit": "inch",
        "timezone": "America/New_York", "forecast_days": 16,
    }
    if model:
        q["models"] = model
    return "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(q)


def parse_open_meteo(d):
    daily = (d or {}).get("daily") or {}
    days = daily.get("time") or []

    def col(name):
        # With one model selected the keys may carry a model suffix.
        if name in daily:
            vals = daily[name]
        else:
            alt = next((k for k in daily if k.startswith(name + "_")), None)
            vals = daily[alt] if alt else []
        return list(vals) + [None] * (len(days) - len(vals))

    hi, lo = col("temperature_2m_max"), col("temperature_2m_min")
    pp, pr = col("precipitation_probability_max"), col("precipitation_sum")
    return [
        {"target_date": t, "high_f": hi[i], "low_f": lo[i],
         "precip_prob_pct": pp[i], "precip_in": pr[i]}
        for i, t in enumerate(days)
    ]


def fetch_open_meteo(model=None):
    return parse_open_meteo(fetch_json(open_meteo_url(model)))


# ── NWS ──────────────────────────────────────────────────────────────────────
def parse_nws(d):
    periods = ((d or {}).get("properties") or {}).get("periods") or []
    days = {}

    def slot(day):
        return days.setdefault(day, {"high": None, "low": None, "pops": []})

    for p in periods:
        try:
            start = datetime.fromisoformat(p["startTime"]).astimezone(TZ)
        except Exception:
            continue
        temp = num(p.get("temperature"))
        if temp is not None and str(p.get("temperatureUnit", "F")).upper() == "C":
            temp = temp * 9 / 5 + 32
        pop = num((p.get("probabilityOfPrecipitation") or {}).get("value"))
        day0 = start.date()
        if pop is not None:
            slot(day0)["pops"].append(pop)
        if p.get("isDaytime"):
            slot(day0)["high"] = temp
        else:
            low_day = day0 if start.hour < 12 else day0 + timedelta(days=1)
            slot(low_day)["low"] = temp

    out = []
    for day in sorted(days):
        s = days[day]
        out.append({
            "target_date": day.isoformat(),
            "high_f": s["high"], "low_f": s["low"],
            "precip_prob_pct": max(s["pops"]) if s["pops"] else None,
            "precip_in": None,  # NWS period forecasts give no rainfall amount
        })
    return out


def fetch_nws():
    hdr = {"Accept": "application/geo+json"}
    pts = fetch_json(f"https://api.weather.gov/points/{LAT},{LON}", headers=hdr)
    url = ((pts or {}).get("properties") or {}).get("forecast")
    if not url:
        return []
    return parse_nws(fetch_json(url, headers=hdr))


# ── Logging ──────────────────────────────────────────────────────────────────
def build_rows(source, forecasts, now):
    rows = []
    log_date = now.date()
    for f in forecasts:
        try:
            target = date.fromisoformat(str(f["target_date"])[:10])
        except Exception:
            continue
        lead = (target - log_date).days
        if lead < 0 or lead > MAX_LEAD:
            continue
        vals = {k: num(f.get(k)) for k in ("high_f", "low_f", "precip_prob_pct", "precip_in")}
        if all(v is None for v in vals.values()):
            continue
        rows.append({
            "log_date": log_date.isoformat(),
            "logged_et": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "source": source,
            "target_date": target.isoformat(),
            "lead_days": lead,
            **{k: (round(v, 2) if v is not None else "") for k, v in vals.items()},
        })
    return rows


def existing_keys(path):
    keys = set()
    if path.exists():
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                keys.add((r.get("log_date"), r.get("source"), r.get("target_date")))
    return keys


def main():
    now = datetime.now(TZ)
    path = Path(LOG_FILE)
    keys = existing_keys(path)

    sources = [
        ("open-meteo-ecmwf", lambda: fetch_open_meteo("ecmwf_ifs025")),
        ("open-meteo-gfs", lambda: fetch_open_meteo("gfs_seamless")),
        ("nws", fetch_nws),
    ]

    new_rows, report = [], []
    for name, loader in sources:
        forecasts = loader()
        rows = [r for r in build_rows(name, forecasts, now)
                if (r["log_date"], r["source"], r["target_date"]) not in keys]
        new_rows.extend(rows)
        report.append((name, f"{len(rows)} new rows" if rows else
                       "no new rows" if forecasts else "NO DATA (see the notes below)"))

    if new_rows:
        write_header = not path.exists() or path.stat().st_size == 0
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if write_header:
                w.writeheader()
            w.writerows(new_rows)

    print(f"Forecast logger — {now.strftime('%Y-%m-%d %H:%M %Z')}")
    for name, msg in report:
        print(f"  {name:18s} {msg}")
    for e in errors:
        print(f"  note: {e}")

    # Fail loudly only if a whole run produced nothing AND nothing exists for today.
    got_something = bool(new_rows) or any(k[0] == now.date().isoformat() for k in keys)
    if not got_something:
        print("No forecasts could be saved this run.")
        sys.exit(1)


if __name__ == "__main__":
    main()
