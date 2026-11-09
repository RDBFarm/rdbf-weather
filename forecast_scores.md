# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (128 days on file, through 2026-11-08) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.3 | 3.3 | 3.2 | 3.8 | 4.3 | 4.2 | 5.1 | 1.0* | — |
| open-meteo-ecmwf | 3.4 | 3.0 | 3.5 | 3.9 | 4.4 | 5.8 | 5.2 | 5.7 | 8.2 |
| open-meteo-gfs | 2.9 | 3.4 | 3.5 | 3.6 | 3.2 | 4.6 | 6.0 | 5.1 | 8.1 |
| persistence | 6.2 | 7.4 | 7.9 | 8.7 | 7.5 | 6.7 | 6.0 | 7.5 | 8.3 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.2 | -3.0 | -3.0 | -3.2 | -2.5 | -2.3 | -2.2 | -1.0* | — |
| open-meteo-ecmwf | -3.3 | -2.9 | -3.2 | -3.3 | -3.2 | -3.1 | -2.6 | -2.8 | -6.5 |
| open-meteo-gfs | -2.8 | -3.2 | -3.2 | -3.5 | -3.2 | -4.3 | -4.3 | -3.5 | -6.4 |
| persistence | 2.2 | 2.0 | 2.1 | 2.4 | 1.9 | 1.4 | 1.8 | 2.2 | 1.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 2.9 | 3.0 | 3.6 | 4.7 | 5.9 | 6.7 | — |
| open-meteo-ecmwf | 4.0 | 4.2 | 4.4 | 4.6 | 4.6 | 4.6 | 5.7 | 6.7 | 6.3 |
| open-meteo-gfs | 3.1 | 3.6 | 3.2 | 3.6 | 4.1 | 5.2 | 5.8 | 5.4 | 8.8 |
| persistence | 4.3 | 6.7 | 8.2 | 8.4 | 8.0 | 8.1 | 7.9 | 8.6 | 10.3 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.063 | 0.079 | 0.057 | 0.025 | 0.033 | 0.048 | 0.068 | 0.000* | — |
| open-meteo-ecmwf | 0.018 | 0.047 | 0.055 | 0.035 | 0.025 | 0.044 | 0.050 | 0.073 | 0.120 |
| open-meteo-gfs | 0.083 | 0.074 | 0.056 | 0.036 | 0.028 | 0.038 | 0.042 | 0.058 | 0.103 |
| persistence | 0.176 | 0.320 | 0.333 | 0.261 | 0.227 | 0.238 | 0.250 | 0.263 | 0.333 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 88 | 88 | 92 | 96 | 100 | 95 | 90 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 92 | 96 | 95 | 90 | 90 | 95 | 86 |
| open-meteo-gfs | 81 | 88 | 92 | 91 | 95 | 90 | 95 | 89 | 87 |
| persistence | 82 | 68 | 67 | 74 | 77 | 76 | 75 | 74 | 67 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.02 | 0.01 | 0.01 | 0.13 | 0.03 | 0.12 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.09 | 0.16 | 0.14 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 17 | 25 | 24 | 23 | 22 | 21 | 20 | 1 | 0 |
| open-meteo-ecmwf | 16 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 101 |
| open-meteo-gfs | 16 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 105 |
| persistence | 17 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 105 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
