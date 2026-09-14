# RDBF Weather Pre-Processor

The weather component of **RDBF**, the farm automation system for **Red Devil
Bison Farm** (Poolesville, MD).

**The main system is [`RDBFarm/rdbf-app`](https://github.com/RDBFarm/rdbf-app)** —
the farm's records (herd, land, equipment, people, places, and the append-only
logs of what has happened to each) and the app that reads them. Its `SPEC.md` is
the design document for the whole system, and it governs this repository too.
Start there.

This repository is one input to that system, and nothing else lives here. It
runs on GitHub Actions twice a day, aggregates five free weather sources into a
single file the debrief can read with one request, and keeps a permanent daily
history. `rdbf-app` copies the output into its own `docs/data/` half an hour
after each run; it consumes this work rather than duplicating it.

An earlier version of this file called this repository "the home for RDBF's farm
automation" and said more components would grow alongside it. That was true when
weather was the only piece. It is not true now, and it left this repository with
no pointer to the system it feeds.

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

The cron **asks** for 09:35 and 21:35 UTC — 5:35 AM and 5:35 PM Eastern in
summer, 4:35 in winter, because the schedule is fixed UTC and Eastern is not.

**It does not get them.** Over the whole recorded history — every run since
2026-08-28 — **3 of 38 scheduled runs arrived on time**. The median is 3h11m
late and the worst was 11h24m. The morning slot is the bad one; the evening
slot usually lands within two hours. In practice the archive is written
around 9:40 AM and 7:20 PM Eastern.

These figures are **not maintained here**. `rdbf-app` measures them from
`ops/run_log.json` and shows them on its feed page, which is the number to
trust — a figure typed into a README is right on the day it is typed. (An
earlier version of this paragraph gave an average of 2h14m and a worst case
of 7h14m over the fortnight to 2026-09-13. Both were correct for that
window and neither matches the record as a whole, which is the point.)

This is the same throttling that made an hourly schedule useless, and that
is now measured too rather than remembered: for the sixteen hours the cron
was set to hourly on 2026-09-08, **thirteen of the sixteen slots produced no
run at all** — four ran, at 06:29, 11:40, 16:49 and 17:01 UTC. Every missed
run in the entire record falls inside that window. See the comment in
`weather.yml`.

**So why twice a day.** Not for freshness, which this job gave up on: "now"
comes from the Worker asking the station when someone opens a page. The two
runs exist so that **a dropped or badly delayed run has a second chance the
same day**, because what this job produces is the daily archive, and an
archive has to be complete rather than current.

It is working, and this is the strongest evidence in the record. As at
2026-09-14 the archive holds 72 rows across 72 calendar days: no gaps, no
duplicates. Thirty-five runs landed late and thirteen never landed at all,
and **every calendar day still closed**. The second run is what absorbed
that.

A second, weaker reason is sometimes given for the evening run — that it
catches the Drought Monitor map, which publishes Thursdays around noon
Central. True, and not the reason to keep it: that argument justifies a run on
Thursdays and this one earns its place every day. **Do not cut the evening run
to Thursdays.** The drop protection is the point and it is load-bearing.

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
