# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (129 days on file, through 2026-11-09) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.2 | 3.1 | 3.7 | 4.1 | 4.1 | 5.0 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.1 | 3.6 | 3.9 | 4.4 | 5.8 | 5.0 | 5.9 | 8.0 |
| open-meteo-gfs | 2.9 | 3.5 | 3.4 | 3.5 | 3.2 | 4.4 | 5.9 | 5.2 | 8.1 |
| persistence | 6.2 | 7.2 | 8.0 | 8.8 | 7.7 | 6.9 | 5.7 | 7.3 | 8.3 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -2.9 | -3.0 | -3.1 | -2.4 | -2.3 | -2.3 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -2.9 | -3.3 | -3.4 | -3.2 | -3.2 | -2.5 | -3.1 | -6.5 |
| open-meteo-gfs | -2.8 | -3.3 | -3.2 | -3.4 | -2.9 | -4.1 | -4.3 | -3.7 | -6.5 |
| persistence | 2.2 | 1.8 | 2.4 | 2.8 | 2.3 | 1.9 | 1.7 | 2.2 | 2.3 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.0 | 3.1 | 3.6 | 4.5 | 5.9 | 6.7 | — |
| open-meteo-ecmwf | 4.0 | 4.4 | 4.7 | 4.8 | 4.8 | 4.8 | 5.9 | 6.8 | 6.2 |
| open-meteo-gfs | 3.1 | 3.6 | 3.4 | 3.6 | 4.2 | 5.3 | 5.7 | 5.6 | 8.7 |
| persistence | 4.3 | 6.7 | 8.7 | 9.2 | 8.1 | 7.9 | 7.7 | 8.3 | 9.9 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.076 | 0.054 | 0.024 | 0.031 | 0.046 | 0.067 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.045 | 0.053 | 0.033 | 0.023 | 0.042 | 0.049 | 0.073 | 0.124 |
| open-meteo-gfs | 0.083 | 0.072 | 0.054 | 0.035 | 0.026 | 0.036 | 0.041 | 0.060 | 0.099 |
| persistence | 0.176 | 0.308 | 0.360 | 0.292 | 0.217 | 0.227 | 0.238 | 0.250 | 0.312 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 88 | 92 | 96 | 100 | 95 | 90 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 92 | 96 | 96 | 91 | 90 | 95 | 86 |
| open-meteo-gfs | 81 | 88 | 92 | 92 | 96 | 91 | 95 | 90 | 88 |
| persistence | 82 | 69 | 64 | 71 | 78 | 77 | 76 | 75 | 69 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.02 | 0.01 | 0.01 | 0.13 | 0.03 | 0.12 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.09 | 0.17 | 0.13 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 26 | 25 | 24 | 23 | 22 | 21 | 1 | 0 |
| open-meteo-ecmwf | 16 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 107 |
| open-meteo-gfs | 16 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 112 |
| persistence | 17 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 112 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
