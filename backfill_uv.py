#!/usr/bin/env python3
"""One-off repair of the uv_peak column in weather_history.csv.

Until the peak-window fix, uv_peak was read from a forecast array that begins at
the current hour. The 5:35 PM run therefore only ever saw the tail of the day and
overwrote the morning run's correct value, so every archived peak is understated
(the whole archive topped out at 0.9 across 43 summer days).

This rewrites uv_peak from Open-Meteo's daily uv_index_max — the same field the
fixed fetch_weather.py now uses for live collection, so a repaired row and a
freshly collected one come from the same place.

Only the uv_peak column is touched. A date the API cannot cover is left exactly
as it is and reported, never guessed.

    python3 backfill_uv.py           # dry run: print the changes, write nothing
    python3 backfill_uv.py --write   # apply them
"""
import csv
import json
import sys
import urllib.request
from datetime import date, datetime

HISTORY_FILE = "weather_history.csv"
LAT, LON = 39.151, -77.462
USER_AGENT = "RDBF-preprocessor (github.com/rdbfarm)"
MAX_PAST_DAYS = 92          # Open-Meteo's ceiling on the forecast endpoint


def fetch_uv_max(oldest):
    """{date -> uv_index_max} from oldest through today, or None on failure."""
    past_days = (date.today() - oldest).days + 1
    if past_days > MAX_PAST_DAYS:
        print(f"!! {oldest} is {past_days} days back; the API only serves "
              f"{MAX_PAST_DAYS}. Earlier dates cannot be repaired from here.")
        past_days = MAX_PAST_DAYS

    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={LAT}&longitude={LON}"
           "&daily=uv_index_max&timezone=America%2FNew_York"
           f"&past_days={past_days}&forecast_days=1")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as r:
            daily = (json.load(r).get("daily") or {})
        return {d: v for d, v in zip(daily.get("time") or [],
                                     daily.get("uv_index_max") or [])}
    except Exception as e:
        print(f"!! Open-Meteo request failed: {type(e).__name__}: {e}")
        return None


def main():
    write = "--write" in sys.argv

    with open(HISTORY_FILE, newline="") as f:
        reader = csv.DictReader(f)
        columns, rows = reader.fieldnames, list(reader)
    if not rows:
        print("weather_history.csv has no rows; nothing to do.")
        return 0

    uv = fetch_uv_max(date.fromisoformat(min(r["date"] for r in rows)))
    if uv is None:
        return 1

    changed, unchanged, skipped = [], 0, []
    for r in rows:
        new = uv.get(r["date"])
        if new is None:
            skipped.append(r["date"])
            continue
        old = r["uv_peak"]
        if old == "" or abs(float(old) - float(new)) >= 0.05:
            changed.append((r["date"], old or "(blank)", new))
            r["uv_peak"] = new
        else:
            unchanged += 1

    print(f"\n{len(rows)} rows | {len(changed)} to change | {unchanged} already "
          f"correct | {len(skipped)} not covered by the API")
    if changed:
        print(f"\n  {'date':12} {'was':>8}  ->  {'now':>6}")
        for d, o, n in changed:
            print(f"  {d:12} {str(o):>8}  ->  {n:>6}")
        vals = [n for _, _, n in changed]
        print(f"\n  new peaks range {min(vals)} to {max(vals)}")
    if skipped:
        print(f"\n  left untouched (no API value): {', '.join(skipped)}")

    if not write:
        print("\nDry run — nothing written. Re-run with --write to apply.")
        return 0
    if not changed:
        print("\nNothing to write.")
        return 0

    with open(HISTORY_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns)
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["date"]):
            w.writerow(r)
    print(f"\nWrote {len(changed)} repaired values to {HISTORY_FILE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
