# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (133 days on file, through 2026-11-13) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.0 | 3.0 | 3.5 | 4.1 | 4.2 | 4.9 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.0 | 3.5 | 4.0 | 4.3 | 5.4 | 5.0 | 5.4 | 8.4 |
| open-meteo-gfs | 2.9 | 3.7 | 3.3 | 3.6 | 3.0 | 4.3 | 6.0 | 5.8 | 8.7 |
| persistence | 6.2 | 7.6 | 8.3 | 8.5 | 7.6 | 7.0 | 6.7 | 8.2 | 8.4 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -2.7 | -2.8 | -3.0 | -2.7 | -2.6 | -2.5 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -2.9 | -3.2 | -3.6 | -3.3 | -3.2 | -2.9 | -2.9 | -6.4 |
| open-meteo-gfs | -2.8 | -3.5 | -3.0 | -3.5 | -2.7 | -4.1 | -4.7 | -4.6 | -7.3 |
| persistence | 2.2 | 2.0 | 2.2 | 2.6 | 2.7 | 2.8 | 3.3 | 3.3 | 3.1 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 2.9 | 3.0 | 3.6 | 4.5 | 5.7 | 6.5 | — |
| open-meteo-ecmwf | 4.0 | 4.2 | 4.6 | 4.7 | 4.8 | 4.7 | 5.9 | 6.6 | 6.4 |
| open-meteo-gfs | 3.1 | 3.7 | 3.4 | 4.1 | 4.3 | 5.1 | 6.1 | 5.9 | 8.4 |
| persistence | 4.3 | 6.8 | 8.7 | 9.2 | 8.8 | 8.7 | 8.3 | 8.2 | 8.9 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.076 | 0.052 | 0.028 | 0.046 | 0.065 | 0.088 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.054 | 0.056 | 0.032 | 0.035 | 0.055 | 0.071 | 0.091 | 0.152 |
| open-meteo-gfs | 0.083 | 0.080 | 0.063 | 0.034 | 0.041 | 0.053 | 0.069 | 0.084 | 0.123 |
| persistence | 0.176 | 0.300 | 0.345 | 0.321 | 0.296 | 0.231 | 0.240 | 0.292 | 0.300 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 90 | 93 | 96 | 96 | 88 | 88 | 100* | — |
| open-meteo-ecmwf | 100 | 90 | 93 | 96 | 93 | 88 | 84 | 92 | 83 |
| open-meteo-gfs | 81 | 87 | 90 | 93 | 93 | 85 | 92 | 88 | 85 |
| persistence | 82 | 70 | 66 | 68 | 70 | 77 | 76 | 71 | 70 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.02 | 0.02 | 0.04 | 0.02 | 0.01 | 0.11 | 0.03 | 0.10 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.05 | 0.12 | 0.16 | 0.12 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 30 | 29 | 28 | 27 | 26 | 25 | 1 | 0 |
| open-meteo-ecmwf | 16 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 131 |
| open-meteo-gfs | 16 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 140 |
| persistence | 17 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 140 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
