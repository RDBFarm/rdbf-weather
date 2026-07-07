# RDBF Weather Pre-Processor

Automated weather data pipeline for Red Devil Bison Farm (Poolesville, MD).
Runs on GitHub Actions twice a day, aggregates five free weather sources into
a single file the farm debrief can read with one request, and keeps a permanent
daily history.

---

## What it does

Every run, `fetch_weather.py`:

1. Fetches from five sources (see below).
2. Applies the farm's data-integrity rules (no invented values; missing data is
   null, never guessed; all times converted to Eastern).
3. Writes **`weather_summary.json`** — a fresh snapshot of current conditions,
   soil temps, forecast, alerts, UV, drought status, and yesterday's report.
4. Appends one row per day to **`weather_history.csv`** — a permanent archive
   that never loses past days.

The debrief only ever needs to read `weather_summary.json`. The CSV is for
history, trends, and charts.

---

## The five sources

| # | Source | Provides |
|---|--------|----------|
| 1 | Weather Underground station **KMDPOOLE58** | Current conditions, actual rain totals, yesterday's daily summary |
| 2 | Open-Meteo | Soil temps (0cm/6cm), precip forecast, sunrise/sunset |
| 3 | NWS Alerts (api.weather.gov) | Active weather alerts (test messages filtered out) |
| 4 | currentuvindex.com | Hourly UV forecast (converted UTC → Eastern) |
| 5 | US Drought Monitor | County drought status, FIPS 24031 (Montgomery Co MD) |

No API key is needed for sources 2–5. Source 1 (Weather Underground) requires
a key, stored as a GitHub secret named `WU_API_KEY` — never in any file.

---

## Files in this repo

| File | What it is | Who writes it |
|------|-----------|---------------|
| `fetch_weather.py` | The aggregator script | You (upload) |
| `.github/workflows/weather.yml` | The schedule + commit logic | You (upload) |
| `weather_summary.json` | Latest snapshot (overwritten each run) | The script |
| `weather_history.csv` | Permanent daily archive (append-only) | The script |
| `SETUP.md` | One-time setup steps | Reference |
| `README.md` | This file | Reference |

You only ever upload/edit the first two. The bottom two are generated
automatically — do not edit them by hand.

---

## Schedule

Runs automatically at:
- **5:35 AM Eastern** (morning refresh)
- **5:35 PM Eastern** (evening refresh — this one catches the fresh Drought
  Monitor map, which publishes Thursdays around noon Central)

You can also trigger a run any time: **Actions → RDBF Weather Pre-Processor →
Run workflow**.

---

## Data-integrity rules (built into the script)

- **Nothing is estimated.** If a source fails or a value is missing, it's
  written as `null` and logged in `data_integrity.errors_this_run` — never
  guessed or filled with a plausible-looking number.
- **All times are Eastern.** UTC values (UV, alerts) are converted before writing.
- **UV crossings are sanity-checked** against sunrise/sunset; impossible values
  are nulled rather than trusted.
- **Rain vs snow:** rain totals come from your station (actual); snow/freezing
  rain come from Open-Meteo and are labeled as estimates needing confirmation.
  Fog is never counted as precipitation.
- **NWS test messages are filtered** out of the real alert count (but recorded
  in `test_messages_filtered` so nothing is silently dropped).
- **History is append-only.** `weather_history.csv` keeps one row per day and
  never loses a past day. Re-running a day updates that day's row.

---

## `weather_history.csv` columns

Today's snapshot plus yesterday's verified station summary:

- **Today:** date, temp_f, humidity_pct, precip_today_in, soil_0cm_f,
  soil_6cm_f, soil_trend_7day, precip_type_today, nws_active_alerts, uv_peak
- **Drought:** drought_week_ending, drought_d0_pct … drought_d4_pct
  (cumulative — D1 = % of county in moderate drought *or worse*)
- **Yesterday (from station):** yest_date, yest_temp_high_f, yest_temp_low_f,
  yest_humidity_avg_pct, yest_wind_avg_mph, yest_wind_gust_high_mph,
  yest_precip_total_in

---

## How to update the system

1. Make edits to `fetch_weather.py` or `weather.yml`.
2. In GitHub: navigate to the file's folder, **Add file → Upload files**, drag
   the new version in (it replaces the existing one), commit to `main`.
   - `fetch_weather.py` lives in the **repo root**.
   - `weather.yml` lives in **`.github/workflows/`** — make sure the breadcrumb
     shows that folder before committing, or you'll create a stray copy.
3. **Run workflow** once to test.

**Tip:** when pasting code, make sure the file starts with its real first line
(`name:` for the workflow, `#!/usr/bin/env python3` for the script) — don't
include any Markdown code-fence markers like ```` ```yaml ````.

---

## Troubleshooting

**A run failed / no new row appeared.**
Open the failed run: Actions → click the run → **fetch-weather** job → expand
the steps. Two common cases:
- *Push rejected / merge conflict* → two runs collided. The current workflow
  handles this by syncing to the remote and regenerating; if you see an old
  rebase-based version, upload the latest `weather.yml`.
- *`Archived …` line present but no commit* → the workflow didn't stage the CSV;
  confirm the commit step includes both `weather_summary.json` and
  `weather_history.csv`.

**Drought values are null.**
The Drought Monitor query is date-format sensitive (no leading zeros) and only
publishes Thursdays. The evening run picks up the fresh map. If it's persistently
null, check `data_integrity.errors_this_run` in the JSON.

**A duplicate date appears in the CSV.**
Rare, usually from a failed-run recovery. Safe to fix by hand: edit
`weather_history.csv` on GitHub, delete the extra line, commit. Re-running the
day also refreshes it.

**Never edit `weather_summary.json` or `weather_history.csv` by hand** except to
remove a stray duplicate row — the script owns them and will overwrite/rebuild.

---

## Location constants

Set at the top of `fetch_weather.py`:
- Latitude / Longitude: 39.151, -77.462 (Poolesville, MD)
- Station: KMDPOOLE58
- County FIPS: 24031 (Montgomery County, MD)

---

*Part of the RDBF farm debrief system. The weather snapshot feeds the daily
voice debrief; the history archive feeds trend charts.*
