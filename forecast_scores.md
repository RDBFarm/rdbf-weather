# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (124 days on file, through 2026-11-04) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.5 | 3.5 | 4.0 | 4.2 | 4.3 | 4.9 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.3 | 3.6 | 4.3 | 4.4 | 5.6 | 5.5 | 5.9 | 8.0 |
| open-meteo-gfs | 3.2 | 3.1 | 3.6 | 3.9 | 3.5 | 4.6 | 5.9 | 5.1 | 7.8 |
| persistence | 5.7 | 7.2 | 7.3 | 7.9 | 7.1 | 7.1 | 7.1 | 7.6 | 8.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.2 | -3.3 | -3.6 | -3.0 | -2.6 | -2.3 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.1 | -3.5 | -3.7 | -3.4 | -3.4 | -2.4 | -2.8 | -6.3 |
| open-meteo-gfs | -3.1 | -2.9 | -3.3 | -3.8 | -3.4 | -4.2 | -4.6 | -3.5 | -5.7 |
| persistence | 1.7 | 1.0 | 1.6 | 2.5 | 2.7 | 2.1 | 1.8 | 2.3 | 2.3 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.0 | 3.0 | 3.1 | 3.7 | 4.9 | 6.4 | 7.1 | — |
| open-meteo-ecmwf | 4.4 | 4.7 | 4.9 | 4.9 | 4.5 | 4.4 | 5.8 | 7.2 | 5.9 |
| open-meteo-gfs | 3.3 | 3.6 | 3.5 | 3.7 | 3.9 | 4.8 | 6.2 | 5.3 | 8.7 |
| persistence | 4.0 | 4.8 | 6.8 | 7.7 | 7.1 | 7.5 | 7.4 | 8.3 | 9.2 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.055 | 0.047 | 0.020 | 0.019 | 0.035 | 0.048 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.019 | 0.022 | 0.013 | 0.006 | 0.010 | 0.018 | 0.038 | 0.044 |
| open-meteo-gfs | 0.095 | 0.056 | 0.031 | 0.023 | 0.002 | 0.011 | 0.019 | 0.025 | 0.027 |
| persistence | 0.133 | 0.190 | 0.250 | 0.211 | 0.167 | 0.176 | 0.188 | 0.200 | 0.273 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 95 | 95 | 95 | 100 | 94 | 94 | 100* | — |
| open-meteo-ecmwf | 100 | 95 | 95 | 100 | 100 | 100 | 100 | 100 | 99 |
| open-meteo-gfs | 79 | 90 | 95 | 95 | 100 | 100 | 100 | 100 | 100 |
| persistence | 87 | 81 | 75 | 79 | 83 | 82 | 81 | 80 | 73 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.08 | 0.06 | 0.13 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 21 | 20 | 19 | 18 | 17 | 16 | 1 | 0 |
| open-meteo-ecmwf | 14 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 76 |
| open-meteo-gfs | 14 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 77 |
| persistence | 15 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 77 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
