#!/usr/bin/env python3
"""Fill in drought_at_farm for the days recorded before the point query existed.

weather_history.csv started carrying the farm's own drought class on
2026-09-05. Every earlier row has the county percentages and a blank where the
farm's class should be. The US Drought Monitor keeps an archive of its weekly
polygons, so those blanks can be filled from the same source that fills new
rows, rather than left as a hole in the middle of the record.

Dry run by default — it prints what it would write and changes nothing:

    python3 backfill_drought_at_farm.py
    python3 backfill_drought_at_farm.py --write

Nothing is inferred. A week the archive cannot answer for stays blank, because
a blank says "not known" and any value would say something stronger than the
data supports.
"""
import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

HISTORY = Path("weather_history.csv")
COLUMN = "drought_at_farm"
LAT, LON = 39.151, -77.462
UA = {"User-Agent": "RDBF-weather backfill (github.com/RDBFarm/rdbf-weather)"}
TIMEOUT = 60

# Confirmed reachable by probe_drought_sources.py. The archive holds one
# polygon set per week going back to 2000.
ARCHIVE = ("https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services"
           "/USDM_archive/FeatureServer")

# Candidate names for the two fields that matter. The service is not ours and
# does not promise these names, so the layer is asked what it actually has and
# the answer is matched against these rather than assumed.
DATE_FIELDS = ("ddate", "DDATE", "date", "Date", "DATE", "MapDate", "mapdate", "validstart")
CLASS_FIELDS = ("dm", "DM", "drought_class", "gridcode", "GRIDCODE")


def get(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  ! {url.split('?')[0]} -> {type(e).__name__}: {e}")
        return None


def find_layer():
    """Return (layer_url, date_field, class_field) or None.

    Walks the service's layers and picks the first that carries both a date
    field and a drought-class field under a name we recognise. Reporting which
    layer and which fields were chosen matters as much as the answer: a silent
    guess here would poison sixty rows at once.
    """
    svc = get(f"{ARCHIVE}?f=json")
    if not svc:
        return None
    layers = (svc.get("layers") or []) + (svc.get("tables") or [])
    if not layers:
        print("  ! service lists no layers")
        return None

    for lyr in layers:
        url = f"{ARCHIVE}/{lyr['id']}"
        meta = get(f"{url}?f=json")
        if not meta:
            continue
        names = {f["name"] for f in meta.get("fields", [])}
        date_f = next((n for n in DATE_FIELDS if n in names), None)
        class_f = next((n for n in CLASS_FIELDS if n in names), None)
        print(f"  layer {lyr['id']} '{meta.get('name')}' — "
              f"date: {date_f or 'none found'}, class: {class_f or 'none found'}")
        if date_f and class_f:
            return url, date_f, class_f
    print("  ! no layer carried both a date and a drought-class field")
    return None


def fetch_weeks(layer_url, date_f, class_f, first, last):
    """Every (map date, worst class) covering the farm between two dates.

    The polygons nest — a point in D2 also sits inside D1 and D0 — so the worst
    class covering the point is the one that describes it.
    """
    params = urllib.parse.urlencode({
        "geometry": f"{LON},{LAT}",
        "geometryType": "esriGeometryPoint",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "where": (f"{date_f} >= DATE '{first.isoformat()}' "
                  f"AND {date_f} <= DATE '{last.isoformat()}'"),
        "outFields": f"{date_f},{class_f}",
        "returnGeometry": "false",
        "orderByFields": date_f,
        "resultRecordCount": 2000,
        "f": "json",
    })
    data = get(f"{layer_url}/query?{params}")
    if not data or "error" in data:
        if data and "error" in data:
            print(f"  ! service error: {data['error']}")
        return None
    if data.get("exceededTransferLimit"):
        print("  ! response was truncated by the service — refusing a partial answer")
        return None

    weeks = {}
    for feat in data.get("features", []):
        a = feat.get("attributes") or {}
        raw, cls = a.get(date_f), a.get(class_f)
        if raw is None or cls is None:
            continue
        try:
            cls = int(cls)
        except (TypeError, ValueError):
            continue
        if not 0 <= cls <= 4:
            continue
        # Esri returns dates as epoch milliseconds, UTC.
        try:
            day = datetime.utcfromtimestamp(int(raw) / 1000).date()
        except (TypeError, ValueError, OSError):
            continue
        weeks[day] = max(weeks.get(day, -1), cls)
    return weeks


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="apply the changes (default is a dry run)")
    args = ap.parse_args()

    rows = list(csv.DictReader(HISTORY.open(newline="")))
    if not rows:
        print("weather_history.csv is empty")
        return 1
    if COLUMN not in rows[0]:
        print(f"weather_history.csv has no {COLUMN} column — run fetch_weather.py first")
        return 1

    need = [r for r in rows if not (r.get(COLUMN) or "").strip()]
    print(f"{len(rows)} rows, {len(need)} without {COLUMN}")
    if not need:
        print("Nothing to backfill.")
        return 0

    first = datetime.strptime(min(r["date"] for r in need), "%Y-%m-%d").date()
    last = datetime.strptime(max(r["date"] for r in need), "%Y-%m-%d").date()
    print(f"Range to cover: {first} to {last}")

    print("\nFinding the archive layer:")
    found = find_layer()
    if not found:
        return 1
    layer_url, date_f, class_f = found
    print(f"  using {layer_url} ({date_f}, {class_f})")

    # Map dates are Tuesdays and a map stands until the next one, so reach back
    # a week before the first day needing an answer.
    print("\nQuerying the farm's point:")
    weeks = fetch_weeks(layer_url, date_f, class_f, first - timedelta(days=8), last)
    if weeks is None:
        return 1
    if not weeks:
        print("  ! the point matched no archived polygon in that range")
        print("    That would mean no drought anywhere near the farm all summer,")
        print("    which the county figures contradict. Treating it as a failed")
        print("    lookup rather than as an answer.")
        return 1
    print(f"  {len(weeks)} map week(s): "
          + ", ".join(f"{d} D{c}" for d, c in sorted(weeks.items())))

    # Each day takes the most recent map on or before it. A map published on a
    # Tuesday describes the ground until the next one lands.
    ordered = sorted(weeks)
    changes = []
    for r in need:
        day = datetime.strptime(r["date"], "%Y-%m-%d").date()
        applicable = [d for d in ordered if d <= day]
        if not applicable:
            continue                      # no map covers this day; leave it blank
        cls = weeks[applicable[-1]]
        changes.append((r, f"D{cls}", applicable[-1]))

    print(f"\n{len(changes)} row(s) would be filled, "
          f"{len(need) - len(changes)} left blank for want of a map:")
    for r, val, src in changes:
        print(f"  {r['date']}  {val}   (map of {src}, county D1 {r.get('drought_d1_pct')}%)")

    if not args.write:
        print("\nDry run — nothing written. Re-run with --write to apply.")
        return 0

    for r, val, _ in changes:
        r[COLUMN] = val
    with HISTORY.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {len(changes)} row(s) to {HISTORY}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
