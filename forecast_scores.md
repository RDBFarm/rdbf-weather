# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (127 days on file, through 2026-11-07) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.4 | 3.4 | 3.3 | 4.0 | 4.3 | 4.4 | 5.2 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.0 | 3.6 | 4.0 | 4.5 | 5.8 | 5.4 | 5.7 | 8.3 |
| open-meteo-gfs | 3.0 | 3.5 | 3.6 | 3.7 | 3.2 | 4.6 | 6.1 | 5.3 | 8.1 |
| persistence | 6.3 | 7.2 | 7.7 | 8.5 | 7.3 | 7.0 | 6.2 | 7.9 | 8.4 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.3 | -3.1 | -3.2 | -3.3 | -2.5 | -2.4 | -2.2 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -2.9 | -3.3 | -3.5 | -3.2 | -2.9 | -2.8 | -2.6 | -6.5 |
| open-meteo-gfs | -3.0 | -3.3 | -3.4 | -3.5 | -3.2 | -4.3 | -4.4 | -3.7 | -6.3 |
| persistence | 2.6 | 1.6 | 1.6 | 1.9 | 1.4 | 1.5 | 1.7 | 2.3 | 1.5 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 3.0 | 3.1 | 3.7 | 4.8 | 6.2 | 6.9 | — |
| open-meteo-ecmwf | 4.1 | 4.3 | 4.5 | 4.6 | 4.5 | 4.5 | 5.7 | 6.8 | 6.5 |
| open-meteo-gfs | 3.1 | 3.6 | 3.2 | 3.7 | 4.0 | 5.0 | 5.7 | 5.6 | 8.9 |
| persistence | 4.4 | 6.4 | 7.7 | 8.6 | 8.3 | 8.4 | 8.2 | 8.8 | 10.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.067 | 0.082 | 0.059 | 0.026 | 0.034 | 0.047 | 0.069 | 0.000* | — |
| open-meteo-ecmwf | 0.019 | 0.049 | 0.058 | 0.037 | 0.026 | 0.046 | 0.053 | 0.076 | 0.127 |
| open-meteo-gfs | 0.088 | 0.078 | 0.059 | 0.038 | 0.029 | 0.039 | 0.044 | 0.060 | 0.109 |
| persistence | 0.188 | 0.292 | 0.304 | 0.273 | 0.238 | 0.250 | 0.263 | 0.278 | 0.357 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 88 | 91 | 95 | 100 | 95 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 91 | 95 | 95 | 90 | 89 | 94 | 85 |
| open-meteo-gfs | 80 | 88 | 91 | 91 | 95 | 90 | 95 | 89 | 86 |
| persistence | 81 | 71 | 70 | 73 | 76 | 75 | 74 | 72 | 64 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.03 | 0.01 | 0.01 | 0.14 | 0.04 | 0.13 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.09 | 0.16 | 0.14 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 16 | 24 | 23 | 22 | 21 | 20 | 19 | 1 | 0 |
| open-meteo-ecmwf | 15 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 95 |
| open-meteo-gfs | 15 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 98 |
| persistence | 16 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 98 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
