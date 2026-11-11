# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (130 days on file, through 2026-11-10) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.2 | 3.1 | 3.6 | 4.0 | 4.1 | 5.1 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.1 | 3.7 | 3.9 | 4.4 | 5.6 | 4.9 | 5.7 | 8.3 |
| open-meteo-gfs | 2.9 | 3.4 | 3.4 | 3.5 | 3.1 | 4.3 | 6.0 | 5.4 | 8.7 |
| persistence | 6.2 | 7.3 | 8.2 | 8.6 | 7.6 | 6.8 | 5.6 | 7.3 | 8.1 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -2.9 | -3.0 | -3.1 | -2.4 | -2.4 | -2.5 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -3.0 | -3.4 | -3.4 | -3.2 | -3.1 | -2.5 | -3.0 | -6.8 |
| open-meteo-gfs | -2.8 | -3.2 | -3.1 | -3.4 | -2.8 | -4.0 | -4.5 | -3.9 | -7.2 |
| persistence | 2.2 | 1.4 | 1.9 | 2.8 | 2.5 | 2.0 | 1.8 | 1.7 | 2.1 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.0 | 3.0 | 3.1 | 3.6 | 4.5 | 5.8 | 6.7 | — |
| open-meteo-ecmwf | 4.0 | 4.6 | 4.8 | 4.9 | 5.0 | 4.9 | 6.0 | 7.0 | 6.4 |
| open-meteo-gfs | 3.1 | 3.7 | 3.4 | 3.8 | 4.3 | 5.5 | 6.1 | 5.5 | 8.6 |
| persistence | 4.3 | 6.9 | 8.8 | 9.7 | 9.0 | 8.1 | 7.6 | 8.3 | 9.8 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.073 | 0.052 | 0.023 | 0.030 | 0.044 | 0.064 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.043 | 0.051 | 0.032 | 0.023 | 0.040 | 0.046 | 0.070 | 0.127 |
| open-meteo-gfs | 0.083 | 0.069 | 0.052 | 0.034 | 0.025 | 0.034 | 0.039 | 0.057 | 0.096 |
| persistence | 0.176 | 0.296 | 0.346 | 0.320 | 0.250 | 0.217 | 0.227 | 0.238 | 0.294 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 89 | 92 | 96 | 100 | 96 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 92 | 96 | 96 | 91 | 91 | 95 | 86 |
| open-meteo-gfs | 81 | 89 | 92 | 92 | 96 | 91 | 95 | 90 | 88 |
| persistence | 82 | 70 | 65 | 68 | 75 | 78 | 77 | 76 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.02 | 0.01 | 0.01 | 0.12 | 0.03 | 0.11 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.03 | 0.09 | 0.17 | 0.13 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 27 | 26 | 25 | 24 | 23 | 22 | 1 | 0 |
| open-meteo-ecmwf | 16 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 113 |
| open-meteo-gfs | 16 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 119 |
| persistence | 17 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 119 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
