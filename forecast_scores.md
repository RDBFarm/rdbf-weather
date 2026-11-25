# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (144 days on file, through 2026-11-24) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 2.9 | 2.8 | 2.7 | 3.2 | 3.8 | 3.9 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.0 | 2.9 | 3.3 | 3.8 | 4.1 | 5.0 | 5.3 | 5.8 | 8.1 |
| open-meteo-gfs | 2.7 | 3.6 | 3.6 | 3.9 | 3.5 | 5.0 | 6.1 | 6.4 | 8.4 |
| persistence | 6.1 | 7.7 | 8.9 | 9.6 | 9.1 | 8.7 | 7.9 | 8.7 | 8.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.8 | -2.6 | -2.5 | -2.8 | -2.8 | -2.9 | -2.8 | -1.0* | — |
| open-meteo-ecmwf | -2.9 | -2.7 | -3.0 | -3.4 | -3.4 | -3.4 | -3.5 | -3.8 | -5.1 |
| open-meteo-gfs | -2.7 | -3.3 | -3.3 | -3.8 | -3.2 | -4.8 | -5.0 | -5.5 | -6.6 |
| persistence | 2.6 | 1.3 | 1.6 | 2.1 | 1.9 | 1.7 | 1.8 | 2.2 | 3.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 8.0* | 3.5 | 3.5 | 3.5 | 3.8 | 4.4 | 5.2 | 5.8 | — |
| open-meteo-ecmwf | 4.6 | 5.0 | 5.2 | 5.2 | 5.2 | 5.2 | 5.7 | 6.4 | 6.7 |
| open-meteo-gfs | 3.3 | 4.4 | 4.1 | 4.8 | 5.0 | 5.3 | 5.8 | 5.9 | 8.2 |
| persistence | 4.9 | 7.3 | 9.1 | 9.6 | 9.2 | 8.9 | 8.7 | 8.8 | 10.4 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.052 | 0.074 | 0.055 | 0.029 | 0.037 | 0.050 | 0.063 | 0.000* | — |
| open-meteo-ecmwf | 0.014 | 0.046 | 0.051 | 0.038 | 0.037 | 0.045 | 0.052 | 0.070 | 0.128 |
| open-meteo-gfs | 0.066 | 0.065 | 0.060 | 0.047 | 0.039 | 0.041 | 0.051 | 0.060 | 0.087 |
| persistence | 0.143 | 0.244 | 0.275 | 0.256 | 0.237 | 0.189 | 0.194 | 0.257 | 0.276 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 90 | 92 | 95 | 97 | 92 | 92 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 95 | 95 | 92 | 92 | 89 | 94 | 87 |
| open-meteo-gfs | 85 | 88 | 90 | 92 | 92 | 89 | 94 | 91 | 90 |
| persistence | 86 | 76 | 72 | 74 | 76 | 81 | 81 | 74 | 72 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.06 | 0.06 | 0.12 | 0.08 | 0.03 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.06 | 0.05 | 0.07 | 0.09 | 0.11 | 0.09 |
| persistence | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 21 | 41 | 40 | 39 | 38 | 37 | 36 | 1 | 0 |
| open-meteo-ecmwf | 20 | 41 | 40 | 39 | 38 | 37 | 36 | 35 | 199 |
| open-meteo-gfs | 20 | 41 | 40 | 39 | 38 | 37 | 36 | 35 | 217 |
| persistence | 21 | 41 | 40 | 39 | 38 | 37 | 36 | 35 | 217 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
