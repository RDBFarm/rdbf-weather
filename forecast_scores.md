# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (119 days on file, through 2026-10-30) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4.0 | 3.9 | 4.0 | 4.6 | 4.4 | 4.1 | 4.3 | 1.0* | — |
| open-meteo-ecmwf | 3.9 | 3.8 | 4.0 | 4.6 | 5.0 | 5.7 | 5.2 | 6.2 | 8.5 |
| open-meteo-gfs | 3.3 | 3.4 | 3.9 | 4.4 | 3.5 | 4.5 | 5.2 | 3.8 | 7.5 |
| persistence | 5.3 | 6.7 | 6.6 | 7.9 | 8.0 | 7.5 | 8.2 | 10.3 | 10.8 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.8 | -3.9 | -4.0 | -4.6 | -4.4 | -4.1 | -3.9 | -1.0* | — |
| open-meteo-ecmwf | -3.7 | -3.6 | -4.0 | -4.6 | -5.0 | -5.7 | -5.2 | -5.7 | -8.5 |
| open-meteo-gfs | -3.2 | -3.3 | -3.5 | -4.4 | -3.5 | -4.5 | -5.2 | -3.0 | -6.4 |
| persistence | 1.3 | 1.3 | 1.9 | 2.6 | 2.0 | 1.8 | 2.4 | 3.3 | 4.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 2.9 | 2.7 | 2.7 | 3.1 | 4.3 | 5.3 | — |
| open-meteo-ecmwf | 4.3 | 4.3 | 4.6 | 4.7 | 3.9 | 3.3 | 4.1 | 4.8 | 4.7 |
| open-meteo-gfs | 3.4 | 3.4 | 3.2 | 3.3 | 3.4 | 3.5 | 4.2 | 3.9 | 7.5 |
| persistence | 3.8 | 5.1 | 7.6 | 8.6 | 8.8 | 9.3 | 9.3 | 10.7 | 13.0 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.083 | 0.058 | 0.053 | 0.025 | 0.003 | 0.002 | 0.002 | 0.000* | — |
| open-meteo-ecmwf | 0.023 | 0.025 | 0.029 | 0.017 | 0.006 | 0.008 | 0.007 | 0.011 | 0.039 |
| open-meteo-gfs | 0.111 | 0.074 | 0.041 | 0.030 | 0.002 | 0.002 | 0.001 | 0.001 | 0.012 |
| persistence | 0.154 | 0.250 | 0.333 | 0.286 | 0.231 | 0.250 | 0.273 | 0.300 | 0.429 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 85 | 94 | 93 | 93 | 100 | 100 | 100 | 100* | — |
| open-meteo-ecmwf | 100 | 94 | 93 | 100 | 100 | 100 | 100 | 100 | 98 |
| open-meteo-gfs | 75 | 88 | 93 | 93 | 100 | 100 | 100 | 100 | 100 |
| persistence | 85 | 75 | 67 | 71 | 77 | 75 | 73 | 70 | 57 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.03 |
| open-meteo-gfs | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.04 |
| persistence | 0.03 | 0.04 | 0.03 | 0.02 | 0.02 | 0.03 | 0.03 | 0.03 | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 13 | 16 | 15 | 14 | 13 | 12 | 11 | 1 | 0 |
| open-meteo-ecmwf | 12 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 42 |
| open-meteo-gfs | 12 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 42 |
| persistence | 13 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 42 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
