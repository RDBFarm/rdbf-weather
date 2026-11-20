#!/usr/bin/env python3
"""
Red Devil Bison Farm — Official Station Observations

Saves Dulles airport's (KIAD) official daily high, low and wind, so the
ensemble forecasts logged for Dulles (ensemble_log.py, place KIAD) can be
scored against an official station beside the farm's own. Added 2026-11-20
(the owner: "add Dulles to the log"): at the farm the forecasts' highs ran
4-7°F cool and calm nights 5°F warm, and only a second station can say how
much of that is the farm station's spot rather than the forecast.

The numbers are the National Weather Service's daily climate report for
Dulles (product CLIIAD, from the Sterling office), read through the Iowa
Environmental Mesonet's archive of NWS products, which gives it parsed. Each
row keeps the NWS product id, so any value can be checked against the report
itself. One row per day, appended to station_obs.csv:

    date, station, high_f, low_f, wind_avg_mph, wind_max_mph, gust_max_mph,
    nws_product, saved_et

  high_f / low_f   the day's official highest and lowest temperature
  wind_avg_mph     the day's average wind speed
  wind_max_mph     the highest two-minute wind
  gust_max_mph     the highest gust

Data-integrity rules (same as fetch_weather.py)
  - Nothing is estimated. A value the report did not give is left blank.
  - The NWS climate day is midnight to midnight local STANDARD time, so in
    summer it runs 1 AM to 1 AM Eastern; the farm station's day is midnight
    to midnight. Said here, not corrected.
  - Only a day's final report is saved: one issued after the day ended.
    A report written during the day (an afternoon preliminary) is skipped.
  - One row per (date, station); the first saved stands. Days from the first
    Dulles forecast (2026-11-20) on.
"""

import csv
import json
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/New_York")
LOG_FILE = "station_obs.csv"
STATION = "KIAD"
START = date(2026, 11, 20)     # the first day the ensemble log forecast for Dulles
USER_AGENT = "RDBF-station-obs (github.com/rdbfarm)"
FIELDS = ["date", "station", "high_f", "low_f", "wind_avg_mph", "wind_max_mph", "gust_max_mph", "nws_product", "saved_et"]


def fetch_json(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  note: {url.split('?')[0]} -> {type(e).__name__}: {e}")
        return None


def num(v):
    try:
        if v is None or v == "" or v == "M":
            return ""
        f = float(v)
        return "" if f != f else f
    except (TypeError, ValueError):
        return ""


def issued_et(product):
    """The report's issue time, from its id ("202611200725-KLWX-..." is UTC)."""
    try:
        return datetime.strptime(product[:12], "%Y%m%d%H%M").replace(tzinfo=timezone.utc).astimezone(TZ)
    except (TypeError, ValueError):
        return None


def build_rows(results, have, now):
    """Rows for days not yet saved, from the archive's parsed reports. Pure."""
    rows = []
    for r in sorted(results or [], key=lambda x: x.get("valid") or ""):
        try:
            day = date.fromisoformat(r.get("valid") or "")
        except ValueError:
            continue
        if day < START or day >= now.date() or day.isoformat() in have:
            continue
        issued = issued_et(r.get("product") or "")
        if not issued or issued.date() <= day:          # not the final report
            continue
        row = {"date": day.isoformat(), "station": STATION,
               "high_f": num(r.get("high")), "low_f": num(r.get("low")),
               "wind_avg_mph": num(r.get("average_wind_speed")), "wind_max_mph": num(r.get("highest_wind_speed")),
               "gust_max_mph": num(r.get("highest_gust_speed")),
               "nws_product": r.get("product") or "", "saved_et": now.strftime("%Y-%m-%dT%H:%M:%S%z")}
        if row["high_f"] == "" and row["low_f"] == "":
            continue
        rows.append(row)
        have.add(day.isoformat())
    return rows


def main():
    now = datetime.now(TZ)
    path = Path(LOG_FILE)
    have = set()
    if path.exists():
        with open(path, newline="") as f:
            have = {r["date"] for r in csv.DictReader(f) if r.get("station") == STATION}
    print(f"Station observations — {now.strftime('%Y-%m-%d %H:%M %Z')}")
    rows = []
    for year in sorted({START.year, now.year}):
        d = fetch_json(f"https://mesonet.agron.iastate.edu/json/cli.py?station={STATION}&year={year}")
        rows += build_rows((d or {}).get("results"), have, now)
    if rows:
        fresh = not path.exists() or path.stat().st_size == 0
        with open(path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if fresh:
                w.writeheader()
            w.writerows(rows)
    print(f"  {STATION}: {len(rows)} new day(s)" + (f", {rows[0]['date']} to {rows[-1]['date']}" if rows else ""))
    # Never fails the job: a missing report waits for the next run.


if __name__ == "__main__":
    sys.exit(main())
