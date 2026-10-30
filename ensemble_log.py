#!/usr/bin/env python3
"""
Red Devil Bison Farm — Ensemble Logger

Saves what NOAA's GEFS ensemble (31 runs, 10 days) and ECMWF's ensemble (51
runs, 15 days; since 2026-10-30), both through Open-Meteo, said about the
farm each morning, so that their spread can be scored against what KMDPOOLE58
recorded. Touring Weather Forecast (the trip
site) widens the GEFS temperature spread by measured multiples (1.9 within
36 hours, 1.3 at 4 days) to draw its "likely range"; the data behind those
multiples was not kept, and nobody archives a forecast as it was made a day
or a week ahead (forecast_log.py says why). This keeps it, so the multiples
can be measured again properly, and so it can be asked whether the runs
understate more on windy days than calm ones (the owner, 2026-10-29).

One row per (log_date, model, target_date), appended to ensemble_log.csv:

    log_date, logged_et, model, run_init_et, target_date, lead_days,
    high_mean_f, high_sd_f, low_mean_f, low_sd_f, members,
    site_high_f, site_high_spread_f, site_low_f, site_low_spread_f,
    wind_mean_mph, wind_spread_mph, gust_max_mph,
    runs_wind_mean_mph, runs_wind_sd_mph, runs_gust_max_mph

  high_mean_f / high_sd_f   each run's own highest hourly temperature that
                            day; their average and standard deviation across
                            the runs (low_* the same for the lowest). These
                            compare with the station's daily high and low.
  members                   how many runs gave a full day (all 24 hours)
  model                     ncep_gefs025 (NOAA) or ecmwf_ifs025 (ECMWF)
  site_high_f / _spread_f   what the trip site draws: the warmest hour of the
                            service's average of the runs, and its spread at
                            that hour (site_low_* the coolest)
  wind_mean_mph             the day's average of the service's averaged wind
  wind_spread_mph           the day's average of its published spread
  gust_max_mph              the day's strongest hour of the published gusts
  runs_wind_mean_mph        each run's own average wind speed that day; their
  runs_wind_sd_mph          average and standard deviation across the runs
  runs_gust_max_mph         each run's strongest hourly gust; their average
                            (Added 2026-10-29, the first day: the published
                            average wind looked too low beside its spread,
                            1.8 mph ± 6.4 eight days out, as if averaged as
                            direction and speed together, which cancels when
                            the runs disagree on direction. Both are kept,
                            so the two can be compared. It is the service's
                            averaging, not NOAA's: Open-Meteo works the
                            averages out itself, and ECMWF's falls the same
                            way, 0.76 mph against its runs' 7.5 a week out,
                            2026-10-30.)
  run_init_et               the run the numbers came from

Data-integrity rules (same as fetch_weather.py)
  - Nothing is estimated. A value the service did not give is left blank; a
    day with a missing hour gets no high or low rather than a partial one.
  - All dates and times are Eastern. lead_days = target_date - log_date.
  - One row per (log_date, target_date); the first saved each day stands.
  - Hourly values: a run's daily high is its warmest hour, which can sit a
    little below the true peak a station records. Said here, not corrected.
"""

import csv
import json
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

LAT, LON = 39.151, -77.462  # Poolesville, MD (same as fetch_weather.py)
TZ = ZoneInfo("America/New_York")
LOG_FILE = "ensemble_log.csv"
USER_AGENT = "RDBF-ensemble-logger (github.com/rdbfarm)"
# The ensembles logged: the service's name for each, the name its run times
# are kept under, and how many days it reaches. ECMWF's 51 runs were added
# 2026-10-30 (the owner: "add it to the log"), beside NOAA's 31, to see
# whether their spread behaves better at the farm before the trip site uses
# them. Both arrive with a value every hour; whether the service fills hours
# between the models' own (both, as far as known, publish every 3 hours) is
# not stated, so a run's daily high may sit a little below the true peak.
MODELS = [
    ("ncep_gefs025", "ncep_gefs025", 10),           # NOAA GEFS, 31 runs
    ("ecmwf_ifs025", "ecmwf_ifs025_ensemble", 15),  # ECMWF ENS, 51 runs
]
C_TO_F_SPREAD = 1.8             # the service gives spreads in °C even when °F is asked for (Trip-weather README)

FIELDS = [
    "log_date", "logged_et", "model", "run_init_et", "target_date", "lead_days",
    "high_mean_f", "high_sd_f", "low_mean_f", "low_sd_f", "members",
    "site_high_f", "site_high_spread_f", "site_low_f", "site_low_spread_f",
    "wind_mean_mph", "wind_spread_mph", "gust_max_mph",
    "runs_wind_mean_mph", "runs_wind_sd_mph", "runs_gust_max_mph",
]

errors = []


def fetch_json(url, timeout=60):
    """GET a URL, return parsed JSON or None (never raises)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        reason = ""
        if isinstance(e, urllib.error.HTTPError):
            try:
                reason = json.loads(e.read().decode("utf-8")).get("reason") or ""
            except Exception:
                pass
        errors.append(f"{url.split('?')[0]} -> {type(e).__name__}: {e}" + (f" ({reason})" if reason else ""))
        return None


def ensemble_url(model, hourly, days):
    return "https://ensemble-api.open-meteo.com/v1/ensemble?" + urllib.parse.urlencode({
        "latitude": LAT, "longitude": LON, "models": model, "hourly": hourly,
        "temperature_unit": "fahrenheit", "wind_speed_unit": "mph",
        "timezone": "America/New_York", "forecast_days": days,
    })


def num(v):
    try:
        if v is None or v == "":
            return None
        f = float(v)
        return None if f != f else f
    except (TypeError, ValueError):
        return None


def by_day(times, values):
    """{date: [values for that local day]} — None kept, so a gap is visible."""
    out = {}
    for t, v in zip(times, values):
        out.setdefault(str(t)[:10], []).append(num(v))
    return out


def rnd(v, n=2):
    return "" if v is None else round(v, n)


def build_rows(members_json, mean_json, run_init, now, model="ncep_gefs025"):
    """The day rows from the two responses. Pure: tested with made-up data."""
    mh = (members_json or {}).get("hourly") or {}
    times = mh.get("time") or []
    member_keys = [k for k in mh if k == "temperature_2m" or k.startswith("temperature_2m_member")]
    # The same runs' wind: each run's own day of speeds and gusts.
    runs_wind = {}
    for k in [k for k in mh if k == "wind_speed_10m" or k.startswith("wind_speed_10m_member")]:
        g = mh.get(k.replace("wind_speed_10m", "wind_gusts_10m"))
        gd = by_day(times, g) if g else {}
        for day, vals in by_day(times, mh[k]).items():
            gv = gd.get(day) or []
            if len(vals) == 24 and all(v is not None for v in vals):
                d = runs_wind.setdefault(day, {"mean": [], "gust": []})
                d["mean"].append(statistics.mean(vals))
                if len(gv) == 24 and all(v is not None for v in gv):
                    d["gust"].append(max(gv))
    # Each run's daily high and low, only from a full day of hours.
    per_day = {}
    for k in member_keys:
        for day, vals in by_day(times, mh[k]).items():
            if len(vals) == 24 and all(v is not None for v in vals):
                d = per_day.setdefault(day, {"hi": [], "lo": []})
                d["hi"].append(max(vals)); d["lo"].append(min(vals))

    ah = (mean_json or {}).get("hourly") or {}
    at = ah.get("time") or []
    temp = by_day(at, ah.get("temperature_2m") or [])
    tspr = by_day(at, ah.get("temperature_2m_spread") or [])
    wind = by_day(at, ah.get("wind_speed_10m") or [])
    wspr = by_day(at, ah.get("wind_speed_10m_spread") or [])
    gust = by_day(at, ah.get("wind_gusts_10m") or [])

    rows = []
    for day in sorted(set(per_day) | set(temp)):
        lead = (date.fromisoformat(day) - now.date()).days
        if lead < 0:
            continue
        m = per_day.get(day, {"hi": [], "lo": []})
        sd = lambda xs: statistics.pstdev(xs) if len(xs) > 1 else None
        row = {
            "log_date": now.date().isoformat(), "logged_et": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "model": model, "run_init_et": run_init or "", "target_date": day, "lead_days": lead,
            "high_mean_f": rnd(statistics.mean(m["hi"]) if m["hi"] else None), "high_sd_f": rnd(sd(m["hi"])),
            "low_mean_f": rnd(statistics.mean(m["lo"]) if m["lo"] else None), "low_sd_f": rnd(sd(m["lo"])),
            "members": len(m["hi"]) or "",
        }
        t, s = temp.get(day) or [], tspr.get(day) or []
        if len(t) == 24 and all(v is not None for v in t) and len(s) == 24:
            ih, il = t.index(max(t)), t.index(min(t))
            row.update(site_high_f=rnd(t[ih]), site_low_f=rnd(t[il]),
                       site_high_spread_f=rnd(s[ih] * C_TO_F_SPREAD if s[ih] is not None else None),
                       site_low_spread_f=rnd(s[il] * C_TO_F_SPREAD if s[il] is not None else None))
        w, ws, g = wind.get(day) or [], wspr.get(day) or [], gust.get(day) or []
        if len(w) == 24 and all(v is not None for v in w):
            row["wind_mean_mph"] = rnd(statistics.mean(w))
        if len(ws) == 24 and all(v is not None for v in ws):
            row["wind_spread_mph"] = rnd(statistics.mean(ws))
        if len(g) == 24 and all(v is not None for v in g):
            row["gust_max_mph"] = rnd(max(g))
        rw = runs_wind.get(day)
        if rw and rw["mean"]:
            row["runs_wind_mean_mph"] = rnd(statistics.mean(rw["mean"]))
            row["runs_wind_sd_mph"] = rnd(sd(rw["mean"]))
        if rw and rw["gust"]:
            row["runs_gust_max_mph"] = rnd(statistics.mean(rw["gust"]))
        if all(row.get(k, "") == "" for k in ("high_mean_f", "site_high_f", "wind_mean_mph")):
            continue
        rows.append({k: row.get(k, "") for k in FIELDS})
    return rows


def run_init_et(meta_name):
    meta = fetch_json(f"https://ensemble-api.open-meteo.com/data/{meta_name}/static/meta.json")
    t = (meta or {}).get("last_run_initialisation_time")
    return datetime.fromtimestamp(t, TZ).strftime("%Y-%m-%dT%H:%M%z") if t else None


# Rows written before a column existed: what that column is for them, when it
# is a fact rather than a value (every row before "model" came from GEFS,
# the only model logged then). Anything else is left blank.
BEFORE = {"model": "ncep_gefs025"}


def widen(path):
    """Give rows written before a column existed that column (blank, or its
    BEFORE fact): no row or value is lost, and every row has the header's
    columns."""
    if not path.exists() or path.stat().st_size == 0:
        return
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        if r.fieldnames == FIELDS:
            return
        rows = list(r)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows({k: x.get(k, "") or (BEFORE.get(k, "") if k not in x else "") for k in FIELDS} for x in rows)


def existing_keys(path):
    keys = set()
    if path.exists():
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                keys.add((r.get("log_date"), r.get("model") or BEFORE["model"], r.get("target_date")))
    return keys


def main():
    now = datetime.now(TZ)
    path = Path(LOG_FILE)
    widen(path)
    keys = existing_keys(path)
    print(f"Ensemble logger — {now.strftime('%Y-%m-%d %H:%M %Z')}")
    rows = []
    for model, meta_name, days in MODELS:
        run = run_init_et(meta_name)
        members = fetch_json(ensemble_url(model, "temperature_2m,wind_speed_10m,wind_gusts_10m", days))
        mean = fetch_json(ensemble_url(model + "_ensemble_mean",
                                       "temperature_2m,temperature_2m_spread,wind_speed_10m,wind_speed_10m_spread,wind_gusts_10m", days))
        new = [r for r in build_rows(members, mean, run, now, model) if (r["log_date"], model, r["target_date"]) not in keys]
        rows.extend(new)
        print(f"  {model:14s} run {run or 'unknown':22s} {len(new)} new rows" if new else f"  {model:14s} run {run or 'unknown':22s} no new rows")
    if rows:
        fresh = not path.exists() or path.stat().st_size == 0
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if fresh:
                w.writeheader()
            w.writerows(rows)
    for e in errors:
        print(f"  note: {e}")
    # A missing ensemble must not stop the other forecasts being committed:
    # say so loudly and leave the exit code to the forecast logger.
    if not rows and not any(k[0] == now.date().isoformat() for k in keys):
        print("  No ensemble rows could be saved this run.")


if __name__ == "__main__":
    sys.exit(main())
