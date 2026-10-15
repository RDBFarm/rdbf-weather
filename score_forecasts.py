#!/usr/bin/env python3
"""
Red Devil Bison Farm — Forecast Scorecard

Compares the forecasts saved in forecast_log.csv with what station KMDPOOLE58
actually recorded (the yest_* columns of weather_history.csv), by lead time:
0 = same day ... 7 = a week ahead, plus 8-14 days ahead as one bucket.

Writes forecast_scores.csv (all the numbers) and forecast_scores.md (the tables).

How it scores
  Truth      A date's actual high, low and rain total are the station's "yest_"
             values from the NEXT day's row (the settled daily summary).
  High / Low Mean absolute error in °F (lower is better), average error
             ("bias": + means the forecast ran warm), and % of days within 3°F.
  Rain       Brier score on the rain chance (0 is perfect; always saying 50%
             scores 0.25), and % of days the 50% call was right. A "rain day"
             is 0.01 in or more at the station.
  Baseline   "persistence" = simply repeating the last known actual (what the
             station recorded the day before the forecast was made). A real
             forecaster should beat it, especially at short range.
  Same day   Same-day forecasts logged after noon are left out, because by then
             part of the day has already happened.
  Nothing is estimated: a day missing a value is skipped for that measure, and
  every table reports how many days it rests on. A * marks fewer than 10 days.
"""

import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

HISTORY_FILE = "weather_history.csv"
LOG_FILE = "forecast_log.csv"
OUT_CSV = "forecast_scores.csv"
OUT_MD = "forecast_scores.md"

# Optional: python score_forecasts.py [log_csv] [out_csv] [out_md]
# (the backtest uses this to score backtest_log.csv into backtest_scores.*)
if len(sys.argv) >= 2:
    LOG_FILE = sys.argv[1]
if len(sys.argv) >= 3:
    OUT_CSV = sys.argv[2]
if len(sys.argv) >= 4:
    OUT_MD = sys.argv[3]
BACKTEST = "backtest" in OUT_MD

RAIN_DAY_IN = 0.01
PERSISTENCE = "persistence"
BUCKETS = [str(i) for i in range(8)] + ["8-14"]
MIN_N = 10


def fnum(v):
    try:
        if v is None or str(v).strip() == "":
            return None
        f = float(v)
        return None if f != f else f
    except (TypeError, ValueError):
        return None


def bucket(lead):
    if 0 <= lead <= 7:
        return str(lead)
    if 8 <= lead <= 14:
        return "8-14"
    return None


def load_truth(path=HISTORY_FILE):
    truth = {}
    if not Path(path).exists():
        return truth
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            yd = (r.get("yest_date") or "").strip()
            if not yd:
                continue
            truth[yd] = {
                "high": fnum(r.get("yest_temp_high_f")),
                "low": fnum(r.get("yest_temp_low_f")),
                "precip": fnum(r.get("yest_precip_total_in")),
            }
    return truth


def load_observations(truth, path=LOG_FILE):
    """-> {(source, bucket): [dict(forecast and actual values)]}"""
    obs = defaultdict(list)
    if not Path(path).exists():
        return obs
    pairs = set()  # (log_date, target_date, lead) actually scored, for the baseline
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            target = r.get("target_date")
            actual = truth.get(target)
            if not actual:
                continue
            try:
                lead = int(r["lead_days"])
                logged = datetime.fromisoformat(r["logged_et"])
            except (KeyError, ValueError):
                continue
            b = bucket(lead)
            if b is None:
                continue
            if lead == 0 and logged.hour >= 12:
                continue
            f_pop, f_pr = fnum(r.get("precip_prob_pct")), fnum(r.get("precip_in"))
            if f_pop is None and f_pr is not None:
                # A source that gives only a rain AMOUNT (no chance): treat
                # 0.01 in or more as a 100% rain call, less as 0%. The Brier
                # score then equals that source's plain miss rate.
                f_pop = 100.0 if f_pr >= RAIN_DAY_IN else 0.0
            obs[(r["source"], b)].append({
                "f_high": fnum(r.get("high_f")), "f_low": fnum(r.get("low_f")),
                "f_pop": f_pop, "f_pr": f_pr,
                "a_high": actual["high"], "a_low": actual["low"], "a_pr": actual["precip"],
            })
            pairs.add((r["log_date"], target, lead))

    # Persistence baseline: repeat the last actual known when the forecast was made.
    for log_date, target, lead in pairs:
        try:
            prev = (date.fromisoformat(log_date) - timedelta(days=1)).isoformat()
        except ValueError:
            continue
        last, actual = truth.get(prev), truth.get(target)
        if not last or not actual:
            continue
        rained = None if last["precip"] is None else last["precip"] >= RAIN_DAY_IN
        obs[(PERSISTENCE, bucket(lead))].append({
            "f_high": last["high"], "f_low": last["low"],
            "f_pop": None if rained is None else (100.0 if rained else 0.0),
            "f_pr": last["precip"],
            "a_high": actual["high"], "a_low": actual["low"], "a_pr": actual["precip"],
        })
    return obs


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def summarize(items):
    hi = [(i["f_high"] - i["a_high"]) for i in items
          if i["f_high"] is not None and i["a_high"] is not None]
    lo = [(i["f_low"] - i["a_low"]) for i in items
          if i["f_low"] is not None and i["a_low"] is not None]
    brier, call = [], []
    for i in items:
        if i["f_pop"] is None or i["a_pr"] is None:
            continue
        rained = 1.0 if i["a_pr"] >= RAIN_DAY_IN else 0.0
        brier.append((i["f_pop"] / 100.0 - rained) ** 2)
        call.append(1.0 if (i["f_pop"] >= 50) == (rained == 1.0) else 0.0)
    prm = [abs(i["f_pr"] - i["a_pr"]) for i in items
           if i["f_pr"] is not None and i["a_pr"] is not None]
    return {
        "n_high": len(hi), "high_mae": mean([abs(x) for x in hi]), "high_bias": mean(hi),
        "high_within3_pct": mean([100.0 if abs(x) <= 3 else 0.0 for x in hi]),
        "n_low": len(lo), "low_mae": mean([abs(x) for x in lo]), "low_bias": mean(lo),
        "low_within3_pct": mean([100.0 if abs(x) <= 3 else 0.0 for x in lo]),
        "n_rain": len(brier), "rain_brier": mean(brier),
        "rain_call_correct_pct": None if not call else 100.0 * mean(call),
        "n_precip_amt": len(prm), "precip_mae_in": mean(prm),
    }


def source_order(sources):
    return sorted(sources, key=lambda s: (s == PERSISTENCE, s))


def cell(value, n, nd=1):
    if value is None or not n:
        return "—"
    return f"{value:.{nd}f}" + ("*" if n < MIN_N else "")


def table(title, summaries, sources, key, nkey, nd=1):
    lines = [f"### {title}", "",
             "| Source | " + " | ".join(BUCKETS) + " |",
             "|---|" + "---:|" * len(BUCKETS)]
    for s in sources:
        row = []
        for b in BUCKETS:
            m = summaries.get((s, b))
            row.append(cell(m[key], m[nkey], nd) if m else "—")
        lines.append(f"| {s} | " + " | ".join(row) + " |")
    return lines + [""]


def n_table(summaries, sources):
    lines = ["### Days behind each number (high-temperature count)", "",
             "| Source | " + " | ".join(BUCKETS) + " |",
             "|---|" + "---:|" * len(BUCKETS)]
    for s in sources:
        row = [str(summaries[(s, b)]["n_high"]) if (s, b) in summaries else "0" for b in BUCKETS]
        lines.append(f"| {s} | " + " | ".join(row) + " |")
    return lines + [""]


def main():
    truth = load_truth()
    obs = load_observations(truth)
    summaries = {k: summarize(v) for k, v in obs.items() if v}
    sources = source_order({s for s, _ in summaries})

    # CSV: every number, one row per source and lead bucket.
    cols = ["source", "lead_days", "n_high", "high_mae", "high_bias", "high_within3_pct",
            "n_low", "low_mae", "low_bias", "low_within3_pct", "n_rain", "rain_brier",
            "rain_call_correct_pct", "n_precip_amt", "precip_mae_in"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for s in sources:
            for b in BUCKETS:
                m = summaries.get((s, b))
                if not m:
                    continue
                w.writerow([s, b] + [("" if m[c] is None else (round(m[c], 3) if isinstance(m[c], float) else m[c]))
                                     for c in cols[2:]])

    # Stamped with the newest station day, not the clock: a re-score of the
    # same data then writes the same file, and nothing needs a time zone.
    through = max(truth) if truth else "none"
    md = ["# RDBF forecast scorecard", "",
          f"_Actuals from station KMDPOOLE58 ({len(truth)} days on file, through "
          f"{through}) · lead 0 = same day, 7 = a week ahead._", ""]
    if not sources:
        md += ["No forecast has matured yet. Forecasts are saved by `forecast_log.py`; a "
               "forecast can only be scored once its target day has passed and the station "
               "summary for that day is in `weather_history.csv`. Same-day scores appear "
               "within about two days, 7-day-ahead scores after about a week."]
    else:
        md += table("High temperature — average miss (°F, lower is better)",
                    summaries, sources, "high_mae", "n_high")
        md += table("High temperature — average error (°F, + = forecast ran warm)",
                    summaries, sources, "high_bias", "n_high")
        md += table("Low temperature — average miss (°F, lower is better)",
                    summaries, sources, "low_mae", "n_low")
        md += table("Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)",
                    summaries, sources, "rain_brier", "n_rain", nd=3)
        md += table("Rain — % of days the 50% call was right",
                    summaries, sources, "rain_call_correct_pct", "n_rain", nd=0)
        md += table("Rain amount — average miss (inches, lower is better)",
                    summaries, sources, "precip_mae_in", "n_precip_amt", nd=2)
        md += n_table(summaries, sources)
        if BACKTEST:
            md += ["**Backtest notes.** These are archived model forecasts, not consumer "
                   "apps. Lead N means the value each model gave N x 24 hours before each "
                   "hour of the day. Highs and lows come from hourly values, which can run "
                   "slightly cooler/warmer than the station's true extremes, so look at "
                   "differences between models more than the absolute °F. Models give a "
                   "rain amount, not a chance, so 0.01 in or more counts as a 100% rain "
                   "call and the Brier score is the model's plain miss rate. Same-day "
                   "(lead 0) is not scored: the latest model run already includes "
                   "recent observations, so it is not a fair morning forecast.", ""]
        md += ["`*` = fewer than 10 days, treat as noise. `persistence` repeats the last "
               "known actual; a forecaster that cannot beat it is adding nothing. "
               "A rain day is 0.01 in or more at the station."]
    Path(OUT_MD).write_text("\n".join(md) + "\n")
    print(f"Scored {sum(len(v) for v in obs.values())} forecast-days across "
          f"{len(sources)} sources.")


if __name__ == "__main__":
    main()
