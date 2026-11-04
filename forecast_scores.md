# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (123 days on file, through 2026-11-03) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.5 | 3.6 | 4.1 | 4.2 | 4.2 | 4.8 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.3 | 3.7 | 4.3 | 4.5 | 5.7 | 5.5 | 6.1 | 7.6 |
| open-meteo-gfs | 3.2 | 3.1 | 3.7 | 4.0 | 3.4 | 4.3 | 5.9 | 4.4 | 7.0 |
| persistence | 5.7 | 7.0 | 7.2 | 7.6 | 7.5 | 7.5 | 6.9 | 8.0 | 8.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.2 | -3.4 | -3.6 | -2.9 | -2.4 | -2.0 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.1 | -3.5 | -3.6 | -3.4 | -3.4 | -2.1 | -2.7 | -5.8 |
| open-meteo-gfs | -3.1 | -2.8 | -3.4 | -3.8 | -3.3 | -3.9 | -4.4 | -2.6 | -4.7 |
| persistence | 1.7 | 1.8 | 2.3 | 3.4 | 2.9 | 2.2 | 2.6 | 2.6 | 3.3 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 2.9 | 3.0 | 3.5 | 4.9 | 6.4 | 7.2 | — |
| open-meteo-ecmwf | 4.4 | 4.6 | 4.8 | 4.9 | 4.5 | 4.3 | 6.1 | 7.2 | 5.7 |
| open-meteo-gfs | 3.3 | 3.6 | 3.4 | 3.6 | 3.9 | 4.8 | 6.5 | 5.2 | 8.7 |
| persistence | 4.0 | 4.8 | 6.9 | 7.7 | 7.5 | 7.9 | 7.8 | 8.7 | 9.2 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.046 | 0.042 | 0.020 | 0.008 | 0.029 | 0.043 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.020 | 0.023 | 0.013 | 0.004 | 0.007 | 0.018 | 0.040 | 0.041 |
| open-meteo-gfs | 0.095 | 0.059 | 0.032 | 0.024 | 0.002 | 0.008 | 0.016 | 0.024 | 0.025 |
| persistence | 0.133 | 0.200 | 0.263 | 0.222 | 0.176 | 0.188 | 0.200 | 0.214 | 0.300 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 95 | 95 | 94 | 100 | 94 | 93 | 100* | — |
| open-meteo-ecmwf | 100 | 95 | 95 | 100 | 100 | 100 | 100 | 100 | 99 |
| open-meteo-gfs | 79 | 90 | 95 | 94 | 100 | 100 | 100 | 100 | 100 |
| persistence | 87 | 80 | 74 | 78 | 82 | 81 | 80 | 79 | 70 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.08 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.09 | 0.02 | 0.08 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 20 | 19 | 18 | 17 | 16 | 15 | 1 | 0 |
| open-meteo-ecmwf | 14 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 69 |
| open-meteo-gfs | 14 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 70 |
| persistence | 15 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 70 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
