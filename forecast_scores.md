# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (143 days on file, through 2026-11-23) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.9 | 2.7 | 3.3 | 3.9 | 4.0 | 4.9 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.4 | 3.9 | 4.2 | 5.0 | 5.3 | 5.9 | 8.2 |
| open-meteo-gfs | 2.7 | 3.6 | 3.6 | 3.9 | 3.5 | 5.0 | 6.0 | 6.4 | 8.5 |
| persistence | 5.5 | 7.6 | 8.8 | 9.3 | 8.7 | 8.5 | 7.8 | 8.8 | 8.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.6 | -2.6 | -2.9 | -2.8 | -2.9 | -2.9 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.7 | -3.0 | -3.5 | -3.5 | -3.4 | -3.7 | -3.9 | -5.4 |
| open-meteo-gfs | -2.7 | -3.3 | -3.3 | -3.9 | -3.3 | -4.8 | -4.9 | -5.5 | -6.9 |
| persistence | 1.9 | 1.0 | 1.3 | 1.6 | 1.4 | 1.3 | 1.6 | 2.1 | 3.8 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.4 | 3.4 | 3.4 | 3.7 | 4.3 | 5.1 | 5.6 | — |
| open-meteo-ecmwf | 4.4 | 4.8 | 5.1 | 5.1 | 5.1 | 5.2 | 5.6 | 6.4 | 6.5 |
| open-meteo-gfs | 3.2 | 4.4 | 4.1 | 4.8 | 5.0 | 5.4 | 5.9 | 6.0 | 8.2 |
| persistence | 4.2 | 7.0 | 9.1 | 9.8 | 9.5 | 9.2 | 8.9 | 9.0 | 10.4 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.055 | 0.076 | 0.056 | 0.030 | 0.038 | 0.052 | 0.065 | 0.000* | — |
| open-meteo-ecmwf | 0.015 | 0.047 | 0.052 | 0.039 | 0.037 | 0.047 | 0.054 | 0.072 | 0.126 |
| open-meteo-gfs | 0.070 | 0.067 | 0.062 | 0.048 | 0.040 | 0.042 | 0.052 | 0.062 | 0.088 |
| persistence | 0.150 | 0.250 | 0.282 | 0.263 | 0.243 | 0.194 | 0.200 | 0.265 | 0.281 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 90 | 92 | 95 | 97 | 92 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 95 | 95 | 92 | 92 | 89 | 94 | 87 |
| open-meteo-gfs | 84 | 88 | 90 | 92 | 92 | 89 | 94 | 91 | 90 |
| persistence | 85 | 75 | 72 | 74 | 76 | 81 | 80 | 74 | 72 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.06 | 0.06 | 0.12 | 0.08 | 0.03 | 0.08 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.07 | 0.05 | 0.08 | 0.09 | 0.12 | 0.09 |
| persistence | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 20 | 40 | 39 | 38 | 37 | 36 | 35 | 1 | 0 |
| open-meteo-ecmwf | 19 | 40 | 39 | 38 | 37 | 36 | 35 | 34 | 193 |
| open-meteo-gfs | 19 | 40 | 39 | 38 | 37 | 36 | 35 | 34 | 210 |
| persistence | 20 | 40 | 39 | 38 | 37 | 36 | 35 | 34 | 210 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
