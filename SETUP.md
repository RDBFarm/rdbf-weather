# RDBF Weather Pre-Processor — One-Time Setup (~10 minutes)

After this setup, the weather stack runs itself twice a day (5:35 AM and 5:35 PM
Eastern) and your debrief Shortcut fetches ONE url instead of five.

## What I could not do for you (requires your accounts)

1. Create the GitHub repository (your rdbfarm account)
2. Paste in your Weather Underground API key (it's in your Notes app)

Everything else — code, schedule, data rules — is done and tested.

## Steps

### 1. Create the repo
- Go to github.com (signed in as rdbfarm) → New repository
- Name: `rdbf-weather` → Private → Create

### 2. Add the two files
- In the new repo: **Add file → Create new file**
- Type the filename exactly: `.github/workflows/weather.yml`
  (typing the slashes creates the folders automatically)
- Paste in the contents of weather.yml → Commit
- Repeat: **Add file → Create new file** → name it `fetch_weather.py`
- Paste in the contents of fetch_weather.py → Commit

### 3. Add your Weather Underground key as a secret
- Repo → Settings → Secrets and variables → Actions → New repository secret
- Name: `WU_API_KEY`
- Value: paste the key from your Notes app → Add secret
- (The key never appears in any file or log — this is the secure way.)

### 4. Test it
- Repo → Actions tab → "RDBF Weather Pre-Processor" → Run workflow
- Wait ~1 minute, refresh. Green check = success.
- A `weather_summary.json` file will appear in the repo. Open it and
  check the `data_integrity.errors_this_run` list — it should be empty
  (or explain exactly what failed).

### 5. Point your Shortcut at it
Replace the five weather API calls in the debrief Shortcut with ONE
"Get Contents of URL" action:

    https://raw.githubusercontent.com/rdbfarm/rdbf-weather/main/weather_summary.json

NOTE: for a PRIVATE repo, raw URLs need a token. Two options:
  a) Make the repo public (it contains only weather data — no keys,
     no farm records). Simplest.
  b) Keep it private and add a fine-grained GitHub token as a header
     in the Shortcut. Bring this back to a Claude session if you want
     help with that.

## First-run verification checklist

- [ ] `current_conditions.temp_f` matches your station's live reading
- [ ] `soil_temperature.depth_6cm_f` is a plausible July value (70s–80s)
- [ ] `uv_index.sanity_check_passed` is true
- [ ] `drought_status` populates on the first run; on non-Thursdays
      after that it shows `"carried_forward": true` (by design)
- [ ] `precipitation.past_7day_station_actuals` shows 7 daily entries

## Data-integrity rules built in (from the April session)

- No value is ever estimated. Missing data = null + logged error.
- All times converted to Eastern before writing.
- UV crossing times sanity-checked against sunrise/sunset; failures nulled.
- Rain accumulation from your station (actual); snow/freezing rain from
  Open-Meteo, labeled as estimates needing verbal confirmation.
- Fog (WMO 45–48) is never classified as precipitation.
- Drought Monitor queried Thursdays; carried forward other days.
