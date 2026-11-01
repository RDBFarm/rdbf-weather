# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (120 days on file, through 2026-10-31) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.7 | 3.8 | 3.8 | 4.5 | 4.5 | 4.4 | 4.8 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.6 | 3.8 | 4.3 | 4.8 | 5.6 | 5.7 | 6.7 | 8.0 |
| open-meteo-gfs | 3.1 | 3.3 | 3.8 | 4.1 | 3.3 | 4.4 | 5.7 | 3.6 | 7.4 |
| persistence | 5.9 | 7.1 | 6.4 | 8.1 | 8.1 | 7.3 | 7.8 | 9.5 | 10.2 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.6 | -3.8 | -3.8 | -4.1 | -3.6 | -3.2 | -2.8 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.4 | -3.8 | -4.3 | -4.5 | -4.8 | -3.9 | -4.1 | -7.5 |
| open-meteo-gfs | -3.0 | -3.2 | -3.4 | -4.1 | -3.2 | -3.9 | -3.9 | -3.0 | -5.0 |
| persistence | 2.1 | 2.1 | 2.1 | 3.2 | 2.6 | 2.1 | 2.4 | 3.2 | 5.1 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 3.0 | 2.9 | 3.1 | 3.8 | 4.9 | 5.6 | — |
| open-meteo-ecmwf | 4.6 | 4.5 | 4.7 | 4.8 | 4.1 | 3.7 | 5.0 | 5.3 | 4.7 |
| open-meteo-gfs | 3.4 | 3.5 | 3.2 | 3.4 | 3.7 | 3.9 | 5.0 | 3.8 | 8.0 |
| persistence | 4.1 | 5.1 | 7.5 | 8.3 | 8.4 | 8.7 | 8.8 | 9.8 | 11.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.077 | 0.054 | 0.049 | 0.024 | 0.003 | 0.002 | 0.002 | 0.000* | — |
| open-meteo-ecmwf | 0.022 | 0.023 | 0.027 | 0.016 | 0.005 | 0.007 | 0.007 | 0.010 | 0.034 |
| open-meteo-gfs | 0.102 | 0.069 | 0.038 | 0.028 | 0.002 | 0.002 | 0.001 | 0.001 | 0.012 |
| persistence | 0.143 | 0.235 | 0.312 | 0.267 | 0.214 | 0.231 | 0.250 | 0.273 | 0.408 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 86 | 94 | 94 | 93 | 100 | 100 | 100 | 100* | — |
| open-meteo-ecmwf | 100 | 94 | 94 | 100 | 100 | 100 | 100 | 100 | 98 |
| open-meteo-gfs | 77 | 88 | 94 | 93 | 100 | 100 | 100 | 100 | 100 |
| persistence | 86 | 76 | 69 | 73 | 79 | 77 | 75 | 73 | 59 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 |
| persistence | 0.02 | 0.04 | 0.03 | 0.02 | 0.02 | 0.02 | 0.03 | 0.03 | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 14 | 17 | 16 | 15 | 14 | 13 | 12 | 1 | 0 |
| open-meteo-ecmwf | 13 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 49 |
| open-meteo-gfs | 13 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 49 |
| persistence | 14 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 49 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
