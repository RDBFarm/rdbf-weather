#!/usr/bin/env python3
"""
Red Devil Bison Farm — Weather Pre-Processor
Fetches all five weather sources and writes weather_summary.json.

Sources (per RDBF spec, Session 1, April 2026):
  1. Weather Underground PWS KMDPOOLE58  — current conditions, actual rain accumulation
  2. Open-Meteo                          — soil temps (0cm/6cm), precip history+forecast, weathercode
  3. NWS Alerts                          — active alerts for the farm's coordinates
  4. currentuvindex.com                  — hourly UV forecast (UTC -> America/New_York conversion)
  5. US Drought Monitor                  — county drought status, FIPS 24031 (Thursdays only)

Data-integrity rules (non-negotiable):
  - No value is ever estimated or invented. Missing data = null + a note in "errors".
  - All times converted to America/New_York before being written.
  - UV crossing times sanity-checked against sunrise/sunset. Failures -> null + flag.
  - Rain (WMO 51-67): accumulation from Weather Underground (actual).
    Snow (71-77) / freezing rain (56-57): Open-Meteo values, labeled as estimates.
    Fog (45-48): NOT precipitation.
"""

import csv
import io
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# ── Constants ────────────────────────────────────────────────────────────────
LAT, LON = 39.151, -77.462
STATION_ID = "KMDPOOLE58"
FIPS = "24031"  # Montgomery County, MD
TZ = ZoneInfo("America/New_York")
OUTPUT_FILE = "weather_summary.json"
HISTORY_FILE = "weather_history.csv"
USER_AGENT = "RDBF-weather-preprocessor (github.com/rdbfarm)"

WU_API_KEY = os.environ.get("WU_API_KEY", "").strip()

errors = []  # human-readable list of anything that failed


def fetch_json(url, headers=None, timeout=30):
    """GET a URL, return parsed JSON or None (never raises)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        errors.append(f"{url.split('?')[0]} -> {type(e).__name__}: {e}")
        return None


def fetch_text(url, headers=None, timeout=30):
    """GET a URL, return raw text or None (never raises). For CSV endpoints."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        errors.append(f"{url.split('?')[0]} -> {type(e).__name__}: {e}")
        return None


def load_previous():
    """Load the previous weather_summary.json if present (to carry forward drought data)."""
    try:
        with open(OUTPUT_FILE) as f:
            return json.load(f)
    except Exception:
        return None


# ── 1. Weather Underground (current conditions + actual rain) ───────────────
def get_wu():
    out = {
        "source": STATION_ID,
        "temp_f": None, "humidity_pct": None,
        "wind_mph": None, "wind_dir_deg": None,
        "precip_today_in": None, "precip_rate_in_hr": None,
        "obs_time_local": None,
    }
    if not WU_API_KEY:
        errors.append("WU_API_KEY secret not set — Weather Underground skipped")
        return out
    url = (f"https://api.weather.com/v2/pws/observations/current"
           f"?stationId={STATION_ID}&format=json&units=e&apiKey={WU_API_KEY}")
    data = fetch_json(url)
    if not data:
        return out
    try:
        obs = data["observations"][0]
        imp = obs.get("imperial", {})
        out.update({
            "temp_f": imp.get("temp"),
            "humidity_pct": obs.get("humidity"),
            "wind_mph": imp.get("windSpeed"),
            "wind_dir_deg": obs.get("winddir"),
            "precip_today_in": imp.get("precipTotal"),
            "precip_rate_in_hr": imp.get("precipRate"),
            "obs_time_local": obs.get("obsTimeLocal"),
        })
    except (KeyError, IndexError, TypeError) as e:
        errors.append(f"Weather Underground parse error: {e}")
    return out


def get_wu_7day_precip():
    """Daily precip totals for the past 7 days from the station (actuals)."""
    if not WU_API_KEY:
        return None
    url = (f"https://api.weather.com/v2/pws/dailysummary/7day"
           f"?stationId={STATION_ID}&format=json&units=e&apiKey={WU_API_KEY}")
    data = fetch_json(url)
    if not data:
        return None
    days = []
    try:
        for s in data.get("summaries", []):
            days.append({
                "date": (s.get("obsTimeLocal") or "")[:10] or None,
                "precip_in": s.get("imperial", {}).get("precipTotal"),
            })
    except (TypeError, AttributeError) as e:
        errors.append(f"Weather Underground 7-day parse error: {e}")
        return None
    return days or None


# ── 2. Open-Meteo (soil temps, precip history + forecast, weathercode) ──────
def get_open_meteo():
    # Confirmed-working URL from the April session, plus sunrise/sunset for UV sanity checks.
    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={LAT}&longitude={LON}"
           "&hourly=soil_temperature_0cm,soil_temperature_6cm,snowfall,snow_depth,weathercode,rain"
           "&daily=weathercode,snowfall_sum,rain_sum,precipitation_sum,"
           "precipitation_probability_max,sunrise,sunset"
           "&temperature_unit=fahrenheit&timezone=America%2FNew_York&past_days=7")
    return fetch_json(url)


def latest_non_null(times, values, now_local):
    """Most recent hourly value at or before now (never a future/forecast value)."""
    best = None
    for t, v in zip(times or [], values or []):
        if v is None:
            continue
        ts = datetime.fromisoformat(t).replace(tzinfo=TZ)
        if ts <= now_local:
            best = (ts, v)
    return best


def classify_precip(code):
    """WMO weathercode -> precip type per RDBF rules."""
    if code is None:
        return "unknown"
    if 45 <= code <= 48:
        return "fog_not_precip"
    if code in (56, 57):
        return "freezing_rain"
    if (51 <= code <= 55) or (60 <= code <= 67):
        return "rain"
    if 71 <= code <= 77 or code in (85, 86):
        return "snow"
    if code in (80, 81, 82):
        return "rain"
    if code in (95, 96, 99):
        return "thunderstorm"
    return "none"


# ── 3. NWS Alerts ────────────────────────────────────────────────────────────
def get_nws_alerts():
    out = {"source": "api.weather.gov", "active_count": 0, "alerts": [],
           "frost_or_freeze_active": False}
    data = fetch_json(f"https://api.weather.gov/alerts/active?point={LAT},{LON}",
                      headers={"Accept": "application/geo+json"})
    if data is None:
        out["active_count"] = None
        return out
    for feat in data.get("features", []):
        p = feat.get("properties", {})
        event = p.get("event")
        out["alerts"].append({
            "event": event,
            "severity": p.get("severity"),
            "headline": p.get("headline"),
            "onset": p.get("onset"),
            "ends": p.get("ends"),
        })
        if event and any(w in event.lower() for w in ("frost", "freeze")):
            out["frost_or_freeze_active"] = True
    out["active_count"] = len(out["alerts"])
    return out


# ── 4. UV Index (UTC -> ET conversion + sanity check) ────────────────────────
def get_uv(sunrise_iso, sunset_iso):
    out = {"source": "currentuvindex.com", "timezone": "America/New_York",
           "current_uvi": None, "above_3_time_et": None, "below_3_time_et": None,
           "peak_uvi": None, "peak_time_et": None, "sanity_check_passed": None}
    data = fetch_json(f"https://currentuvindex.com/api/v1/uvi?latitude={LAT}&longitude={LON}")
    if not data:
        return out

    try:
        now_block = data.get("now") or {}
        out["current_uvi"] = now_block.get("uvi")

        today_local = datetime.now(TZ).date()
        points = []
        for item in (data.get("forecast") or []):
            t_utc = datetime.fromisoformat(item["time"].replace("Z", "+00:00"))
            t_local = t_utc.astimezone(TZ)
            if t_local.date() == today_local:
                points.append((t_local, item.get("uvi")))

        if points:
            valid = [(t, u) for t, u in points if u is not None]
            if valid:
                peak_t, peak_u = max(valid, key=lambda x: x[1])
                out["peak_uvi"], out["peak_time_et"] = peak_u, peak_t.strftime("%-I:%M %p")
                above = [t for t, u in valid if u >= 3]
                if above:
                    out["above_3_time_et"] = min(above).strftime("%-I:%M %p")
                    out["below_3_time_et"] = max(above).strftime("%-I:%M %p")

        # Sanity check against physical reality: UV crossings must fall between
        # sunrise and sunset. If they don't, the data is wrong — null it out.
        if sunrise_iso and sunset_iso and out["above_3_time_et"]:
            sunrise = datetime.fromisoformat(sunrise_iso).replace(tzinfo=TZ)
            sunset = datetime.fromisoformat(sunset_iso).replace(tzinfo=TZ)
            first_above = min(above)
            last_above = max(above)
            ok = (sunrise <= first_above <= sunset) and (sunrise <= last_above <= sunset)
            out["sanity_check_passed"] = ok
            if not ok:
                errors.append("UV crossing times failed sunrise/sunset sanity check — nulled")
                out["above_3_time_et"] = out["below_3_time_et"] = None
                out["peak_time_et"] = None
        elif out["above_3_time_et"]:
            out["sanity_check_passed"] = None  # couldn't verify — do not claim it passed
    except Exception as e:
        errors.append(f"UV parse error: {type(e).__name__}: {e}")
    return out


# ── 5. US Drought Monitor (Thursdays only; otherwise carry forward) ─────────
def get_drought(previous):
    today = datetime.now(TZ)
    is_thursday = today.weekday() == 3
    prev_block = (previous or {}).get("drought_status")

    if not is_thursday and prev_block:
        prev_block["carried_forward"] = True
        return prev_block

    out = {"source": "US Drought Monitor", "county": "Montgomery County MD",
           "fips": FIPS, "week_ending": None, "d0_pct": None, "d1_pct": None,
           "d2_pct": None, "d3_pct": None, "d4_pct": None,
           "status_summary": None, "carried_forward": False}

    # This API is finicky about date format: use NO leading zeros (7/2/2026,
    # not 07/02/2026) to match the format that returns data. Window is 21 days
    # so there are always 2-3 weekly records to fall back on — important because
    # the scheduled Thursday-morning run happens before the new map is released
    # (USDM publishes Thursdays ~noon Central); the evening run picks up the fresh one.
    start_dt = today - timedelta(days=21)
    end = f"{today.month}/{today.day}/{today.year}"
    start = f"{start_dt.month}/{start_dt.day}/{start_dt.year}"
    url = ("https://usdmdataservices.unl.edu/api/CountyStatistics/"
           f"GetDroughtSeverityStatisticsByAreaPercent"
           f"?aoi={FIPS}&startdate={start}&enddate={end}&statisticsType=1")

    # Endpoint returns CSV by default (proven-reliable format). Parse it directly.
    text = fetch_text(url)
    if not text:
        errors.append("Drought Monitor: no response from API")
        if prev_block:
            prev_block["carried_forward"] = True
            return prev_block
        return out

    def _pct(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    try:
        rows = [r for r in csv.DictReader(io.StringIO(text)) if r.get("ValidEnd")]
        if not rows:
            errors.append("Drought Monitor returned no data rows for the query window "
                          f"({start}–{end}) — check date range/params")
            if prev_block:
                prev_block["carried_forward"] = True
                return prev_block
            return out

        # Pick the most recent week by ValidEnd (ISO strings sort correctly).
        latest = max(rows, key=lambda r: r.get("ValidEnd", ""))
        out["week_ending"] = latest.get("ValidEnd") or latest.get("MapDate")
        out["d0_pct"] = _pct(latest.get("D0"))
        out["d1_pct"] = _pct(latest.get("D1"))
        out["d2_pct"] = _pct(latest.get("D2"))
        out["d3_pct"] = _pct(latest.get("D3"))
        out["d4_pct"] = _pct(latest.get("D4"))

        # Plain-language summary. Percentages are cumulative: D1 = % of county
        # in Moderate drought OR WORSE, etc. Highest active category wins.
        cats = [("Exceptional (D4)", out["d4_pct"]), ("Extreme (D3)", out["d3_pct"]),
                ("Severe (D2)", out["d2_pct"]), ("Moderate (D1)", out["d1_pct"]),
                ("Abnormally Dry (D0)", out["d0_pct"])]
        worst = next(((name, pct) for name, pct in cats if pct and pct > 0), None)
        if worst is None:
            out["status_summary"] = "No drought or abnormal dryness."
        else:
            name, pct = worst
            out["status_summary"] = f"{pct:.0f}% of county in {name} or worse."
    except Exception as e:
        errors.append(f"Drought Monitor parse error: {type(e).__name__}: {e}")
    return out


# ── Daily archive ────────────────────────────────────────────────────────────
HISTORY_COLUMNS = [
    "date", "temp_f", "humidity_pct", "precip_today_in",
    "soil_0cm_f", "soil_6cm_f", "soil_trend_7day",
    "precip_type_today", "nws_active_alerts",
    "uv_peak", "drought_week_ending",
    "drought_d0_pct", "drought_d1_pct", "drought_d2_pct",
    "drought_d3_pct", "drought_d4_pct",
]


def archive_history(summary):
    """Append one row per DAY to weather_history.csv. Same-day re-runs overwrite
    that day's row so the archive stays one-row-per-day and never duplicates.
    Text-only and tiny (~0.7 MB per year); safe to keep in Git forever."""
    today = summary["generated_et"][:10]  # YYYY-MM-DD
    cc = summary.get("current_conditions", {})
    soil = summary.get("soil_temperature", {})
    precip = summary.get("precipitation", {})
    nws = summary.get("nws_alerts", {})
    uv = summary.get("uv_index", {})
    dr = summary.get("drought_status", {})

    row = {
        "date": today,
        "temp_f": cc.get("temp_f"),
        "humidity_pct": cc.get("humidity_pct"),
        "precip_today_in": cc.get("precip_today_in"),
        "soil_0cm_f": soil.get("surface_0cm_f"),
        "soil_6cm_f": soil.get("depth_6cm_f"),
        "soil_trend_7day": soil.get("trend_7day"),
        "precip_type_today": precip.get("type_today"),
        "nws_active_alerts": nws.get("active_count"),
        "uv_peak": uv.get("peak_uvi"),
        "drought_week_ending": dr.get("week_ending"),
        "drought_d0_pct": dr.get("d0_pct"),
        "drought_d1_pct": dr.get("d1_pct"),
        "drought_d2_pct": dr.get("d2_pct"),
        "drought_d3_pct": dr.get("d3_pct"),
        "drought_d4_pct": dr.get("d4_pct"),
    }

    # Read existing rows (if any), keyed by date.
    existing = {}
    try:
        with open(HISTORY_FILE, newline="") as f:
            for r in csv.DictReader(f):
                existing[r.get("date")] = r
    except FileNotFoundError:
        pass
    except Exception as e:
        errors.append(f"weather_history.csv read error: {type(e).__name__}: {e}")

    existing[today] = {k: ("" if row[k] is None else row[k]) for k in HISTORY_COLUMNS}

    # Write back sorted by date (chronological).
    try:
        with open(HISTORY_FILE, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=HISTORY_COLUMNS)
            w.writeheader()
            for date in sorted(existing):
                w.writerow(existing[date])
        print(f"Archived {today} to {HISTORY_FILE} ({len(existing)} days total)")
    except Exception as e:
        errors.append(f"weather_history.csv write error: {type(e).__name__}: {e}")


# ── Assemble ─────────────────────────────────────────────────────────────────
def main():
    now_local = datetime.now(TZ)
    previous = load_previous()

    wu = get_wu()
    wu_7day = get_wu_7day_precip()
    om = get_open_meteo()
    nws = get_nws_alerts()

    # Soil temperature: most recent non-null hourly reading + 7-day trend
    soil = {"source": "Open-Meteo", "surface_0cm_f": None, "depth_6cm_f": None,
            "reading_time_et": None, "planting_threshold_f": 70,
            "threshold_reached_6cm": None, "trend_7day": None}
    forecast_days, sunrise_iso, sunset_iso = [], None, None
    precip_type_today = "unknown"

    if om:
        h = om.get("hourly", {})
        times = h.get("time", [])
        cur0 = latest_non_null(times, h.get("soil_temperature_0cm"), now_local)
        cur6 = latest_non_null(times, h.get("soil_temperature_6cm"), now_local)
        if cur0:
            soil["surface_0cm_f"] = cur0[1]
            soil["reading_time_et"] = cur0[0].strftime("%Y-%m-%d %-I:%M %p")
        if cur6:
            soil["depth_6cm_f"] = cur6[1]
            soil["threshold_reached_6cm"] = cur6[1] >= 70

        # 7-day 6cm trend: compare average of first vs last 24 available past hours
        s6 = [(datetime.fromisoformat(t).replace(tzinfo=TZ), v)
              for t, v in zip(times, h.get("soil_temperature_6cm") or [])
              if v is not None and datetime.fromisoformat(t).replace(tzinfo=TZ) <= now_local]
        if len(s6) >= 48:
            first_avg = sum(v for _, v in s6[:24]) / 24
            last_avg = sum(v for _, v in s6[-24:]) / 24
            diff = last_avg - first_avg
            soil["trend_7day"] = ("warming" if diff > 1.5 else
                                  "cooling" if diff < -1.5 else "steady")

        d = om.get("daily", {})
        for i, date in enumerate(d.get("time", [])):
            forecast_days.append({
                "date": date,
                "weathercode": (d.get("weathercode") or [None]*99)[i],
                "precip_type": classify_precip((d.get("weathercode") or [None]*99)[i]),
                "precip_sum_mm": (d.get("precipitation_sum") or [None]*99)[i],
                "rain_sum_mm": (d.get("rain_sum") or [None]*99)[i],
                "snowfall_sum_cm": (d.get("snowfall_sum") or [None]*99)[i],
                "precip_prob_pct": (d.get("precipitation_probability_max") or [None]*99)[i],
            })
        today_str = now_local.strftime("%Y-%m-%d")
        for i, date in enumerate(d.get("time", [])):
            if date == today_str:
                precip_type_today = classify_precip((d.get("weathercode") or [None]*99)[i])
                sr = (d.get("sunrise") or [None]*99)[i]
                ss = (d.get("sunset") or [None]*99)[i]
                sunrise_iso, sunset_iso = sr, ss
    else:
        errors.append("Open-Meteo unavailable — soil temps and forecast are null")

    uv = get_uv(sunrise_iso, sunset_iso)
    drought = get_drought(previous)

    # Precipitation block per RDBF source-selection rules
    precip = {
        "type_today": precip_type_today,
        "rule": ("rain -> Weather Underground actuals; snow/freezing rain -> "
                 "Open-Meteo ESTIMATE requiring verbal confirmation; fog is not precip"),
        "today_actual_in": wu.get("precip_today_in") if precip_type_today in ("rain", "thunderstorm", "none", "fog_not_precip") else None,
        "today_estimate_note": ("Open-Meteo estimate — confirm verbally"
                                if precip_type_today in ("snow", "freezing_rain") else None),
        "past_7day_station_actuals": wu_7day,
    }

    summary = {
        "generated_et": now_local.isoformat(timespec="seconds"),
        "run_type": "scheduled",
        "data_integrity": {
            "rules": "No estimated values. Missing data is null, never guessed. All times America/New_York.",
            "errors_this_run": errors,
        },
        "current_conditions": wu,
        "soil_temperature": soil,
        "precipitation": precip,
        "forecast_daily": {"source": "Open-Meteo", "days": forecast_days},
        "nws_alerts": nws,
        "uv_index": uv,
        "drought_status": drought,
    }

    # Archive today's values to the permanent history BEFORE overwriting the
    # snapshot, so nothing is ever lost.
    archive_history(summary)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote {OUTPUT_FILE} at {summary['generated_et']}")
    if errors:
        print("Completed with warnings:")
        for e in errors:
            print(f"  - {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
