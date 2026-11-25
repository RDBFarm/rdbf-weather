#!/usr/bin/env python3
"""
Red Devil Bison Farm — the farm station's 5-minute readings

Saves every reading the farm's own station (Weather Underground KMDPOOLE58)
keeps, about one each five minutes, so a question like "how long was it below
freezing this morning" is answered from the farm's station rather than from
Dulles or a model. Added 2026-11-25, the owner: "yes, save the 5-minute
readings." Until then only one reading per run (the 4:35 AM or PM one) and the
day's high and low were kept.

Each run asks the station for two things:

  observations/all/1day   its readings so far, at five-minute intervals
  history/all (yesterday) yesterday's whole day, at the same intervals, which
                          fills the evening the afternoon run could not see

and appends any reading not already saved to station_readings.csv, one row
per reading:

    obs_time_et, obs_time_utc, temp_avg_f, temp_low_f, temp_high_f,
    dew_point_avg_f, humidity_avg_pct, wind_avg_mph, wind_gust_high_mph,
    wind_dir_avg_deg, precip_rate_in_hr, precip_total_in, qc_status, endpoint

  temp_low_f / temp_high_f   the lowest and highest the station saw in that
                             five minutes; temp_avg_f is its average
  precip_total_in            the day's rain so far, as the station counts it
  qc_status                  the station's own quality flag (-1 not checked,
                             0 failed, 1 passed), kept as given
  endpoint                   which of the two answers the reading came from

Data-integrity rules (same as fetch_weather.py)
  - Nothing is estimated. A value the station did not give is left blank; a
    gap in the readings stays a gap.
  - One row per reading, keyed by its UTC time; the first saved stands.
    A run's rows are in time order, but a morning run adds yesterday's
    evening after rows already saved for it, so sort by obs_time_utc to read.
  - Times are Eastern in obs_time_et, as the station gives them, with the UTC
    time beside them so the two can be checked.
  - It never fails the weather run: an answer that does not come waits for the
    next run, and what went wrong is printed for the run's log.
"""

import csv
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/New_York")
STATION_ID = "KMDPOOLE58"
LOG_FILE = "station_readings.csv"
USER_AGENT = "RDBF-station-readings (github.com/rdbfarm)"
FIELDS = ["obs_time_et", "obs_time_utc", "temp_avg_f", "temp_low_f", "temp_high_f",
          "dew_point_avg_f", "humidity_avg_pct", "wind_avg_mph", "wind_gust_high_mph",
          "wind_dir_avg_deg", "precip_rate_in_hr", "precip_total_in", "qc_status", "endpoint"]


def fetch_json(url, timeout=60):
    """GET a URL, return parsed JSON or None (never raises). Never prints the key."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body.strip() else {}
    except Exception as e:
        print(f"  note: {url.split('?')[0]} -> {type(e).__name__}: {e}")
        return None


def val(v):
    """A value as given, or blank. Never a stand-in."""
    if v is None or v == "":
        return ""
    if isinstance(v, float) and v != v:
        return ""
    return v


def build_rows(observations, endpoint, have):
    """Rows for readings not yet saved, from the station's answer. Pure."""
    rows = []
    for o in observations or []:
        utc = o.get("obsTimeUtc") or ""
        if not utc or utc in have:
            continue
        try:
            when = datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        imp = o.get("imperial") or {}
        row = {
            "obs_time_et": when.astimezone(TZ).strftime("%Y-%m-%dT%H:%M:%S%z"),
            "obs_time_utc": utc,
            "temp_avg_f": val(imp.get("tempAvg")), "temp_low_f": val(imp.get("tempLow")),
            "temp_high_f": val(imp.get("tempHigh")), "dew_point_avg_f": val(imp.get("dewptAvg")),
            "humidity_avg_pct": val(o.get("humidityAvg")), "wind_avg_mph": val(imp.get("windspeedAvg")),
            "wind_gust_high_mph": val(imp.get("windgustHigh")), "wind_dir_avg_deg": val(o.get("winddirAvg")),
            "precip_rate_in_hr": val(imp.get("precipRate")), "precip_total_in": val(imp.get("precipTotal")),
            "qc_status": val(o.get("qcStatus")), "endpoint": endpoint,
        }
        if all(row[k] == "" for k in ("temp_avg_f", "temp_low_f", "temp_high_f")):
            continue
        rows.append(row)
        have.add(utc)
    return rows


def days_to_fill(start, today, have_et):
    """Days from start to yesterday with fewer than 280 readings saved. Pure."""
    count = {}
    for t in have_et:
        count[t[:10]] = count.get(t[:10], 0) + 1
    out, d = [], start
    while d < today:
        if count.get(d.isoformat(), 0) < 280:
            out.append(d)
        d += timedelta(days=1)
    return out


def main():
    key = os.environ.get("WU_API_KEY", "").strip()
    now = datetime.now(TZ)
    # --from YYYY-MM-DD fills earlier days from the station's history, one
    # day per request (backfill-readings.yml; the season from 1 September was
    # filled this way on 2026-11-25). Without it, a run asks for yesterday and
    # today only.
    since = None
    if len(sys.argv) == 3 and sys.argv[1] == "--from":
        since = datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
    print(f"Station readings — {now.strftime('%Y-%m-%d %I:%M %p %Z')}")
    if not key:
        print("  note: WU_API_KEY not set; nothing asked")
        return 0
    path = Path(LOG_FILE)
    have, have_et = set(), []
    if path.exists():
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                have.add(r["obs_time_utc"])
                have_et.append(r["obs_time_et"])
    base = f"stationId={STATION_ID}&format=json&units=e&apiKey={key}"
    if since:
        days = days_to_fill(since, now.date(), have_et)
        asks = [("history/all " + d.strftime("%Y%m%d"),
                 f"https://api.weather.com/v2/pws/history/all?{base}&date={d.strftime('%Y%m%d')}")
                for d in days]
    else:
        yday = (now.date() - timedelta(days=1)).strftime("%Y%m%d")
        asks = [("history/all " + yday, f"https://api.weather.com/v2/pws/history/all?{base}&date={yday}"),
                ("observations/all/1day", f"https://api.weather.com/v2/pws/observations/all/1day?{base}")]
    rows = []
    for i, (name, url) in enumerate(asks):
        if since and i:
            time.sleep(3)     # the station's API allows 30 requests a minute
        d = fetch_json(url)
        got = build_rows((d or {}).get("observations"), name.split(" ")[0], have)
        print(f"  {name}: " + ("no answer" if d is None else
                               f"{len((d or {}).get('observations') or [])} reading(s), {len(got)} new"))
        rows += got
    rows.sort(key=lambda r: r["obs_time_utc"])
    if rows:
        fresh = not path.exists() or path.stat().st_size == 0
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if fresh:
                w.writeheader()
            w.writerows(rows)
        print(f"  saved {len(rows)}, {rows[0]['obs_time_et']} to {rows[-1]['obs_time_et']}")
    return 0  # never fails the weather run


if __name__ == "__main__":
    sys.exit(main())
