# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (132 days on file, through 2026-11-12) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.0 | 3.1 | 3.6 | 4.1 | 4.2 | 5.1 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.1 | 3.6 | 4.2 | 4.4 | 5.6 | 5.1 | 5.7 | 8.5 |
| open-meteo-gfs | 2.9 | 3.6 | 3.4 | 3.7 | 3.0 | 4.5 | 6.2 | 5.8 | 9.0 |
| persistence | 6.2 | 7.2 | 7.8 | 8.3 | 7.4 | 7.0 | 6.0 | 7.5 | 7.8 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -2.8 | -2.9 | -3.1 | -2.7 | -2.6 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -2.9 | -3.3 | -3.7 | -3.4 | -3.3 | -2.9 | -3.0 | -7.1 |
| open-meteo-gfs | -2.8 | -3.4 | -3.1 | -3.5 | -2.8 | -4.2 | -4.8 | -4.5 | -7.7 |
| persistence | 2.2 | 1.4 | 1.5 | 2.3 | 2.3 | 2.6 | 2.5 | 2.3 | 2.2 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 2.9 | 3.0 | 3.6 | 4.5 | 5.7 | 6.6 | — |
| open-meteo-ecmwf | 4.0 | 4.4 | 4.7 | 4.8 | 4.9 | 4.9 | 6.0 | 6.8 | 6.4 |
| open-meteo-gfs | 3.1 | 3.6 | 3.3 | 3.9 | 4.3 | 5.3 | 6.2 | 5.9 | 8.4 |
| persistence | 4.3 | 6.9 | 8.7 | 9.4 | 9.1 | 8.9 | 8.1 | 7.7 | 9.2 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.077 | 0.051 | 0.023 | 0.033 | 0.055 | 0.085 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.046 | 0.055 | 0.032 | 0.026 | 0.048 | 0.061 | 0.090 | 0.159 |
| open-meteo-gfs | 0.083 | 0.083 | 0.064 | 0.035 | 0.029 | 0.044 | 0.066 | 0.086 | 0.129 |
| persistence | 0.176 | 0.310 | 0.357 | 0.333 | 0.308 | 0.240 | 0.208 | 0.261 | 0.316 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 90 | 93 | 96 | 100 | 92 | 88 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 93 | 96 | 96 | 88 | 88 | 91 | 82 |
| open-meteo-gfs | 81 | 86 | 89 | 93 | 96 | 88 | 92 | 87 | 84 |
| persistence | 82 | 69 | 64 | 67 | 69 | 76 | 79 | 74 | 68 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.04 | 0.01 | 0.01 | 0.11 | 0.04 | 0.11 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.03 | 0.08 | 0.15 | 0.13 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 29 | 28 | 27 | 26 | 25 | 24 | 1 | 0 |
| open-meteo-ecmwf | 16 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 125 |
| open-meteo-gfs | 16 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 133 |
| persistence | 17 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 133 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
