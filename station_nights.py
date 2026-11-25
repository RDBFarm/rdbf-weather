#!/usr/bin/env python3
"""
Red Devil Bison Farm — each night's cold, from the farm station's readings

One row per night, worked out from station_readings.csv (the station's own
5-minute readings), so the farm site can say how long each night stayed at or
below freezing and at or below the owner's hard-freeze line. Added 2026-11-25:
the owner wants to follow the hard freezes on the fields with endophyte-
infected fescue, and set the line at 28°F ("28°F", asked whether he meant 25 or
28). 32°F is freezing.

A night runs noon to noon, Eastern, and is named by its morning: the night
of 24 to 25 November is "2026-11-25". A cold spell crosses midnight, and a
calendar day would cut it in two.

    night, readings, first_et, last_et, complete, low_f, low_at_et,
    min_at_or_below_32, min_at_or_below_28, from_32_et, until_32_et

  readings            how many readings the night has
  first_et / last_et  the first and last of them
  complete            yes when the readings run from noon to noon with no gap
                      over 15 minutes; otherwise the minutes are a floor
  low_f, low_at_et    the lowest temp_low_f of the night, and when
  min_at_or_below_N   minutes the 5-minute AVERAGE was at or below N°F. Each
                      reading stands for the time since the one before it, up
                      to 10 minutes; a longer gap counts only 5
  from_32_et          the first reading at or below 32°F, and until_32_et the
                      last, so a reader sees the span as well as the total
  thawed_et           the first reading above 32°F after until_32_et, even if
                      it falls in the next night's readings; blank while it
                      has not thawed, or if no reading after it exists yet.
                      A night with from_32_et and thawed_et froze and thawed

Rules (same as fetch_weather.py): nothing estimated; a night with no readings
has no row; the file is rebuilt whole from station_readings.csv every run, so
a reading that arrives late (yesterday's evening, by the morning run) is
counted in its night.
"""

import csv
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/New_York")
READINGS = "station_readings.csv"
OUT = "station_nights.csv"
LINES = (32, 28)          # freezing, and the owner's hard-freeze line (2026-11-25)
FIELDS = ["night", "readings", "first_et", "last_et", "complete", "low_f", "low_at_et",
          "min_at_or_below_32", "min_at_or_below_28", "from_32_et", "until_32_et", "thawed_et"]


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def night_of(t):
    """The morning that names the night a moment falls in (noon to noon)."""
    return (t + timedelta(hours=12)).date()


def et(t):
    return t.strftime("%Y-%m-%dT%H:%M:%S%z")


def build(rows):
    """Night rows from readings. Pure: rows are dicts as station_readings.csv holds them."""
    pts = []
    for r in rows:
        try:
            t = datetime.strptime(r["obs_time_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone(TZ)
        except (KeyError, ValueError):
            continue
        pts.append((t, num(r.get("temp_avg_f")), num(r.get("temp_low_f"))))
    pts.sort(key=lambda p: p[0])
    nights = {}
    for i, (t, avg, low) in enumerate(pts):
        n = nights.setdefault(night_of(t), {"pts": []})
        gap = (t - pts[i - 1][0]).total_seconds() / 60 if i else None
        n["pts"].append((t, avg, low, gap))
    out = []
    for night in sorted(nights):
        p = nights[night]["pts"]
        start = datetime(night.year, night.month, night.day, 12, tzinfo=TZ) - timedelta(days=1)
        end = start + timedelta(days=1)
        first, last = p[0][0], p[-1][0]
        # The first reading's gap reaches back into the night before; that is
        # fine for the minutes, but coverage asks whether the night STARTED.
        inner_gaps = [g for (_, _, _, g) in p[1:] if g is not None]
        complete = (first - start) <= timedelta(minutes=15) and (end - last) <= timedelta(minutes=15) \
            and all(g <= 15 for g in inner_gaps)
        lows = [(lo, t) for (t, _, lo, _) in p if lo is not None]
        lo, lo_at = min(lows) if lows else (None, None)
        row = {"night": night.isoformat(), "readings": len(p), "first_et": et(first), "last_et": et(last),
               "complete": "yes" if complete else "no",
               "low_f": "" if lo is None else (int(lo) if lo == int(lo) else lo),
               "low_at_et": et(lo_at) if lo_at else ""}
        for line in LINES:
            mins = 0.0
            for (t, avg, _, gap) in p:
                if avg is None or avg > line:
                    continue
                span = gap if gap is not None and gap <= 10 else 5.0
                mins += span
            row[f"min_at_or_below_{line}"] = int(round(mins))
        cold = [t for (t, avg, _, _) in p if avg is not None and avg <= 32]
        row["from_32_et"] = et(cold[0]) if cold else ""
        row["until_32_et"] = et(cold[-1]) if cold else ""
        thaw = ""
        if cold:
            later = next((q for q in pts if q[0] > cold[-1] and q[1] is not None), None)
            if later and later[1] > 32:
                thaw = et(later[0])
        row["thawed_et"] = thaw
        out.append(row)
    return out


def main():
    src = Path(READINGS)
    if not src.exists():
        print("Station nights — no readings yet; nothing written")
        return 0
    with open(src, newline="") as f:
        rows = build(list(csv.DictReader(f)))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"Station nights — {len(rows)} night(s)"
          + (f", {rows[0]['night']} to {rows[-1]['night']}" if rows else ""))
    return 0  # never fails the weather run


if __name__ == "__main__":
    sys.exit(main())
