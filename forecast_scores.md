# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (131 days on file, through 2026-11-11) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.1 | 3.1 | 3.7 | 4.0 | 4.2 | 5.2 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.2 | 3.7 | 3.9 | 4.4 | 5.6 | 4.8 | 5.8 | 8.5 |
| open-meteo-gfs | 2.9 | 3.5 | 3.4 | 3.5 | 3.0 | 4.5 | 6.0 | 5.4 | 9.1 |
| persistence | 6.2 | 7.2 | 8.1 | 8.7 | 7.5 | 6.8 | 5.7 | 7.2 | 7.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -2.9 | -2.9 | -3.1 | -2.5 | -2.5 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -3.0 | -3.4 | -3.5 | -3.3 | -3.3 | -2.6 | -3.2 | -7.1 |
| open-meteo-gfs | -2.8 | -3.3 | -3.1 | -3.4 | -2.7 | -4.2 | -4.5 | -4.0 | -7.6 |
| persistence | 2.2 | 1.1 | 1.6 | 2.3 | 2.6 | 2.2 | 2.0 | 1.9 | 2.0 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.0 | 3.1 | 3.6 | 4.4 | 5.6 | 6.4 | — |
| open-meteo-ecmwf | 4.0 | 4.5 | 4.8 | 4.9 | 5.0 | 5.0 | 6.0 | 6.9 | 6.4 |
| open-meteo-gfs | 3.1 | 3.7 | 3.4 | 3.9 | 4.4 | 5.4 | 6.1 | 5.5 | 8.4 |
| persistence | 4.3 | 6.6 | 8.7 | 9.6 | 9.4 | 8.9 | 7.7 | 8.0 | 9.5 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.071 | 0.051 | 0.023 | 0.029 | 0.042 | 0.061 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.042 | 0.049 | 0.031 | 0.022 | 0.038 | 0.044 | 0.067 | 0.122 |
| open-meteo-gfs | 0.083 | 0.066 | 0.050 | 0.032 | 0.024 | 0.033 | 0.037 | 0.054 | 0.091 |
| persistence | 0.176 | 0.286 | 0.333 | 0.308 | 0.280 | 0.250 | 0.217 | 0.227 | 0.278 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 89 | 93 | 96 | 100 | 96 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 93 | 96 | 96 | 92 | 91 | 95 | 87 |
| open-meteo-gfs | 81 | 89 | 93 | 92 | 96 | 92 | 96 | 91 | 89 |
| persistence | 82 | 71 | 67 | 69 | 72 | 75 | 78 | 77 | 72 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.02 | 0.01 | 0.01 | 0.12 | 0.03 | 0.11 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.03 | 0.08 | 0.16 | 0.13 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 28 | 27 | 26 | 25 | 24 | 23 | 1 | 0 |
| open-meteo-ecmwf | 16 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 119 |
| open-meteo-gfs | 16 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 126 |
| persistence | 17 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 126 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
