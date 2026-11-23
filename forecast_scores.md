# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (142 days on file, through 2026-11-22) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.9 | 2.7 | 3.2 | 3.8 | 3.9 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.3 | 3.9 | 4.1 | 5.0 | 5.1 | 5.8 | 8.3 |
| open-meteo-gfs | 2.7 | 3.5 | 3.5 | 3.8 | 3.4 | 4.8 | 6.0 | 6.1 | 8.3 |
| persistence | 5.5 | 7.7 | 8.9 | 9.5 | 8.9 | 8.5 | 7.7 | 8.5 | 8.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.6 | -2.6 | -2.9 | -2.8 | -2.8 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.7 | -3.0 | -3.5 | -3.3 | -3.3 | -3.4 | -3.7 | -5.4 |
| open-meteo-gfs | -2.7 | -3.3 | -3.2 | -3.7 | -3.2 | -4.6 | -4.9 | -5.2 | -6.7 |
| persistence | 1.9 | 1.1 | 1.3 | 1.5 | 1.4 | 1.6 | 2.0 | 2.6 | 4.1 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.4 | 3.4 | 3.4 | 3.7 | 4.4 | 5.2 | 5.8 | — |
| open-meteo-ecmwf | 4.4 | 4.9 | 5.2 | 5.2 | 5.2 | 5.3 | 5.6 | 6.4 | 6.5 |
| open-meteo-gfs | 3.2 | 4.4 | 4.1 | 4.7 | 4.9 | 5.3 | 6.1 | 5.8 | 8.1 |
| persistence | 4.2 | 6.9 | 8.9 | 9.6 | 9.2 | 8.9 | 8.7 | 8.9 | 10.5 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.055 | 0.077 | 0.058 | 0.030 | 0.038 | 0.052 | 0.067 | 0.000* | — |
| open-meteo-ecmwf | 0.015 | 0.048 | 0.047 | 0.039 | 0.030 | 0.045 | 0.055 | 0.073 | 0.124 |
| open-meteo-gfs | 0.070 | 0.068 | 0.063 | 0.043 | 0.033 | 0.041 | 0.054 | 0.063 | 0.090 |
| persistence | 0.150 | 0.256 | 0.289 | 0.270 | 0.250 | 0.200 | 0.206 | 0.273 | 0.286 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 90 | 92 | 95 | 97 | 91 | 91 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 95 | 95 | 94 | 91 | 88 | 94 | 87 |
| open-meteo-gfs | 84 | 87 | 89 | 92 | 94 | 89 | 94 | 91 | 90 |
| persistence | 85 | 74 | 71 | 73 | 75 | 80 | 79 | 73 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.06 | 0.02 | 0.01 | 0.08 | 0.03 | 0.08 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.07 | 0.05 | 0.08 | 0.09 | 0.12 | 0.09 |
| persistence | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 20 | 39 | 38 | 37 | 36 | 35 | 34 | 1 | 0 |
| open-meteo-ecmwf | 19 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 186 |
| open-meteo-gfs | 19 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 203 |
| persistence | 20 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 203 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
