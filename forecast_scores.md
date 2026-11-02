# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (121 days on file, through 2026-11-01) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.7 | 3.6 | 4.2 | 4.3 | 4.2 | 4.5 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.5 | 3.8 | 4.2 | 4.6 | 5.6 | 5.8 | 6.3 | 7.8 |
| open-meteo-gfs | 3.2 | 3.2 | 3.7 | 4.1 | 3.2 | 4.3 | 5.6 | 3.9 | 7.2 |
| persistence | 5.7 | 7.2 | 6.6 | 7.6 | 8.1 | 7.2 | 7.2 | 8.8 | 9.3 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.7 | -3.6 | -3.9 | -3.3 | -2.8 | -2.4 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.3 | -3.8 | -4.2 | -4.0 | -4.1 | -3.0 | -3.7 | -6.5 |
| open-meteo-gfs | -3.1 | -3.1 | -3.4 | -4.1 | -3.1 | -3.8 | -3.8 | -2.1 | -5.1 |
| persistence | 1.7 | 2.4 | 2.5 | 3.0 | 2.9 | 2.4 | 2.3 | 2.8 | 4.5 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.7 | 2.9 | 2.9 | 3.3 | 4.1 | 5.3 | 6.2 | — |
| open-meteo-ecmwf | 4.4 | 4.5 | 4.7 | 4.9 | 4.4 | 4.2 | 5.5 | 6.1 | 5.0 |
| open-meteo-gfs | 3.3 | 3.6 | 3.2 | 3.5 | 3.7 | 3.8 | 5.2 | 4.4 | 8.0 |
| persistence | 4.0 | 5.1 | 7.2 | 8.0 | 8.0 | 8.5 | 8.4 | 9.5 | 10.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.051 | 0.046 | 0.022 | 0.008 | 0.021 | 0.018 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.022 | 0.025 | 0.015 | 0.005 | 0.008 | 0.011 | 0.026 | 0.036 |
| open-meteo-gfs | 0.095 | 0.065 | 0.036 | 0.026 | 0.002 | 0.008 | 0.006 | 0.006 | 0.016 |
| persistence | 0.133 | 0.222 | 0.294 | 0.250 | 0.200 | 0.214 | 0.231 | 0.250 | 0.375 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 94 | 94 | 94 | 100 | 93 | 100 | 100* | — |
| open-meteo-ecmwf | 100 | 94 | 94 | 100 | 100 | 100 | 100 | 100 | 98 |
| open-meteo-gfs | 79 | 89 | 94 | 94 | 100 | 100 | 100 | 100 | 100 |
| persistence | 87 | 78 | 71 | 75 | 80 | 79 | 77 | 75 | 62 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.05 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.06 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 | 0.04 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 18 | 17 | 16 | 15 | 14 | 13 | 1 | 0 |
| open-meteo-ecmwf | 14 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 56 |
| open-meteo-gfs | 14 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 56 |
| persistence | 15 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 56 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
