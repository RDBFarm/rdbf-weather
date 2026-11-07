# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (126 days on file, through 2026-11-06) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.5 | 3.5 | 4.0 | 4.2 | 4.3 | 5.1 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.2 | 3.7 | 4.2 | 4.5 | 5.6 | 5.6 | 5.8 | 8.4 |
| open-meteo-gfs | 3.2 | 3.6 | 3.6 | 3.7 | 3.3 | 4.8 | 6.2 | 5.5 | 8.6 |
| persistence | 5.7 | 6.8 | 7.3 | 8.1 | 7.5 | 7.0 | 6.3 | 7.4 | 8.2 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.2 | -3.3 | -3.6 | -3.0 | -2.8 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.0 | -3.6 | -3.6 | -3.6 | -3.6 | -2.8 | -3.0 | -7.0 |
| open-meteo-gfs | -3.1 | -3.3 | -3.3 | -3.6 | -3.2 | -4.4 | -4.9 | -4.0 | -6.8 |
| persistence | 1.7 | 1.0 | 0.9 | 1.3 | 1.3 | 1.2 | 1.7 | 1.5 | 0.8 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.0 | 3.1 | 3.6 | 4.8 | 6.1 | 7.0 | — |
| open-meteo-ecmwf | 4.4 | 4.4 | 4.6 | 4.7 | 4.5 | 4.3 | 5.8 | 6.8 | 6.7 |
| open-meteo-gfs | 3.3 | 3.6 | 3.3 | 3.8 | 4.0 | 5.0 | 5.8 | 5.4 | 9.2 |
| persistence | 4.0 | 5.9 | 8.0 | 8.8 | 8.4 | 8.6 | 8.3 | 9.2 | 11.1 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.086 | 0.062 | 0.027 | 0.035 | 0.049 | 0.071 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.051 | 0.060 | 0.038 | 0.027 | 0.046 | 0.054 | 0.074 | 0.120 |
| open-meteo-gfs | 0.095 | 0.081 | 0.061 | 0.040 | 0.030 | 0.040 | 0.044 | 0.058 | 0.114 |
| persistence | 0.133 | 0.261 | 0.318 | 0.286 | 0.250 | 0.263 | 0.278 | 0.294 | 0.385 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 87 | 91 | 95 | 100 | 95 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 91 | 91 | 95 | 95 | 89 | 89 | 94 | 85 |
| open-meteo-gfs | 79 | 87 | 91 | 90 | 95 | 89 | 94 | 88 | 85 |
| persistence | 87 | 74 | 68 | 71 | 75 | 74 | 72 | 71 | 62 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.03 | 0.01 | 0.01 | 0.15 | 0.04 | 0.13 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.10 | 0.09 | 0.15 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 23 | 22 | 21 | 20 | 19 | 18 | 1 | 0 |
| open-meteo-ecmwf | 14 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 89 |
| open-meteo-gfs | 14 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 91 |
| persistence | 15 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 91 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
