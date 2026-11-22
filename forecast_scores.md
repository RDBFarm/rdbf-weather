# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (141 days on file, through 2026-11-21) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.9 | 2.7 | 3.2 | 3.9 | 4.0 | 4.9 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.4 | 3.9 | 4.1 | 5.1 | 5.2 | 5.9 | 8.5 |
| open-meteo-gfs | 2.7 | 3.6 | 3.4 | 3.7 | 3.2 | 4.7 | 6.1 | 6.1 | 8.5 |
| persistence | 5.5 | 7.7 | 9.0 | 9.7 | 9.1 | 8.5 | 7.6 | 8.3 | 9.0 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.6 | -2.6 | -2.9 | -2.8 | -2.9 | -2.8 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.8 | -3.0 | -3.5 | -3.3 | -3.3 | -3.6 | -3.8 | -5.6 |
| open-meteo-gfs | -2.7 | -3.4 | -3.1 | -3.6 | -3.0 | -4.4 | -5.1 | -5.1 | -6.8 |
| persistence | 1.9 | 1.0 | 1.1 | 1.5 | 1.6 | 1.8 | 2.4 | 3.2 | 4.3 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.4 | 3.4 | 3.4 | 3.7 | 4.4 | 5.2 | 5.8 | — |
| open-meteo-ecmwf | 4.4 | 5.0 | 5.3 | 5.3 | 5.3 | 5.3 | 5.6 | 6.4 | 6.6 |
| open-meteo-gfs | 3.2 | 4.4 | 4.2 | 4.8 | 5.0 | 5.4 | 6.2 | 5.9 | 8.1 |
| persistence | 4.2 | 6.6 | 8.6 | 9.2 | 8.8 | 8.6 | 8.5 | 9.0 | 10.6 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.055 | 0.061 | 0.041 | 0.022 | 0.036 | 0.051 | 0.067 | 0.000* | — |
| open-meteo-ecmwf | 0.015 | 0.043 | 0.044 | 0.025 | 0.028 | 0.043 | 0.055 | 0.075 | 0.122 |
| open-meteo-gfs | 0.070 | 0.063 | 0.050 | 0.027 | 0.032 | 0.041 | 0.054 | 0.065 | 0.091 |
| persistence | 0.150 | 0.263 | 0.297 | 0.278 | 0.257 | 0.206 | 0.212 | 0.281 | 0.291 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 92 | 95 | 97 | 97 | 91 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 95 | 97 | 94 | 91 | 88 | 94 | 87 |
| open-meteo-gfs | 84 | 89 | 92 | 94 | 94 | 88 | 94 | 91 | 89 |
| persistence | 85 | 74 | 70 | 72 | 74 | 79 | 79 | 72 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.08 | 0.03 | 0.08 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.09 | 0.12 | 0.09 |
| persistence | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 20 | 38 | 37 | 36 | 35 | 34 | 33 | 1 | 0 |
| open-meteo-ecmwf | 19 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 180 |
| open-meteo-gfs | 19 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 196 |
| persistence | 20 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 196 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
