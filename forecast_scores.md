# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (140 days on file, through 2026-11-20) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 3.0 | 2.8 | 3.3 | 4.0 | 4.2 | 5.0 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 3.0 | 3.4 | 4.0 | 4.2 | 5.2 | 5.3 | 6.0 | 8.7 |
| open-meteo-gfs | 2.7 | 3.7 | 3.4 | 3.7 | 3.3 | 4.7 | 6.2 | 6.1 | 8.7 |
| persistence | 5.5 | 7.7 | 9.1 | 9.8 | 9.1 | 8.4 | 7.4 | 8.2 | 9.2 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.7 | -2.7 | -2.9 | -2.9 | -2.9 | -3.0 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.9 | -3.1 | -3.6 | -3.4 | -3.4 | -3.7 | -4.0 | -5.8 |
| open-meteo-gfs | -2.7 | -3.5 | -3.2 | -3.7 | -3.1 | -4.5 | -5.1 | -5.2 | -7.0 |
| persistence | 1.9 | 0.8 | 1.0 | 1.7 | 1.9 | 2.2 | 2.9 | 3.7 | 4.4 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.4 | 3.5 | 3.4 | 3.7 | 4.5 | 5.3 | 5.9 | — |
| open-meteo-ecmwf | 4.4 | 5.0 | 5.3 | 5.4 | 5.3 | 5.3 | 5.7 | 6.3 | 6.8 |
| open-meteo-gfs | 3.2 | 4.4 | 4.2 | 4.8 | 5.0 | 5.4 | 6.2 | 5.9 | 8.2 |
| persistence | 4.2 | 6.5 | 8.5 | 9.2 | 8.9 | 8.8 | 8.7 | 9.1 | 10.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.055 | 0.061 | 0.042 | 0.022 | 0.037 | 0.052 | 0.069 | 0.000* | — |
| open-meteo-ecmwf | 0.015 | 0.044 | 0.045 | 0.026 | 0.029 | 0.044 | 0.057 | 0.077 | 0.126 |
| open-meteo-gfs | 0.070 | 0.065 | 0.051 | 0.027 | 0.032 | 0.042 | 0.056 | 0.068 | 0.094 |
| persistence | 0.150 | 0.270 | 0.306 | 0.286 | 0.265 | 0.212 | 0.219 | 0.290 | 0.291 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 92 | 94 | 97 | 97 | 91 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 94 | 97 | 94 | 91 | 88 | 94 | 86 |
| open-meteo-gfs | 84 | 89 | 92 | 94 | 94 | 88 | 94 | 90 | 89 |
| persistence | 85 | 73 | 69 | 71 | 74 | 79 | 78 | 71 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.09 | 0.03 | 0.08 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.10 | 0.13 | 0.10 |
| persistence | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 20 | 37 | 36 | 35 | 34 | 33 | 32 | 1 | 0 |
| open-meteo-ecmwf | 19 | 37 | 36 | 35 | 34 | 33 | 32 | 31 | 174 |
| open-meteo-gfs | 19 | 37 | 36 | 35 | 34 | 33 | 32 | 31 | 189 |
| persistence | 20 | 37 | 36 | 35 | 34 | 33 | 32 | 31 | 189 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
