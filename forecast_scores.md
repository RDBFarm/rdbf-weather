# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (125 days on file, through 2026-11-05) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.4 | 3.4 | 4.0 | 4.2 | 4.3 | 5.1 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.2 | 3.6 | 4.3 | 4.5 | 5.7 | 5.8 | 5.6 | 8.3 |
| open-meteo-gfs | 3.2 | 3.3 | 3.5 | 3.7 | 3.4 | 4.5 | 6.3 | 5.4 | 8.3 |
| persistence | 5.7 | 7.0 | 7.6 | 8.0 | 7.5 | 6.7 | 6.6 | 7.8 | 8.4 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.1 | -3.2 | -3.6 | -3.0 | -2.8 | -2.6 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.1 | -3.5 | -3.7 | -3.6 | -3.7 | -2.8 | -2.7 | -6.8 |
| open-meteo-gfs | -3.1 | -3.0 | -3.2 | -3.6 | -3.3 | -4.1 | -5.0 | -3.9 | -6.4 |
| persistence | 1.7 | 0.9 | 1.0 | 1.9 | 1.8 | 1.9 | 1.7 | 1.5 | 1.4 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.0 | 3.0 | 3.1 | 3.8 | 5.0 | 6.5 | 7.2 | — |
| open-meteo-ecmwf | 4.4 | 4.5 | 4.7 | 4.9 | 4.6 | 4.5 | 6.0 | 7.1 | 6.7 |
| open-meteo-gfs | 3.3 | 3.6 | 3.4 | 3.7 | 4.0 | 5.0 | 6.1 | 5.6 | 9.4 |
| persistence | 4.0 | 5.7 | 7.6 | 8.4 | 8.1 | 8.1 | 8.2 | 9.1 | 10.6 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.064 | 0.052 | 0.023 | 0.025 | 0.042 | 0.058 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.018 | 0.021 | 0.016 | 0.013 | 0.032 | 0.039 | 0.050 | 0.084 |
| open-meteo-gfs | 0.095 | 0.058 | 0.035 | 0.027 | 0.014 | 0.027 | 0.031 | 0.045 | 0.075 |
| persistence | 0.133 | 0.227 | 0.286 | 0.250 | 0.211 | 0.222 | 0.235 | 0.250 | 0.333 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 91 | 95 | 95 | 100 | 94 | 94 | 100* | — |
| open-meteo-ecmwf | 100 | 95 | 95 | 100 | 100 | 94 | 94 | 100 | 90 |
| open-meteo-gfs | 79 | 91 | 95 | 95 | 100 | 94 | 100 | 94 | 92 |
| persistence | 87 | 77 | 71 | 75 | 79 | 78 | 76 | 75 | 67 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.03 | 0.02 | 0.03 | 0.00 | 0.00 | 0.12 | 0.01 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.10 | 0.07 | 0.15 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.03 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 22 | 21 | 20 | 19 | 18 | 17 | 1 | 0 |
| open-meteo-ecmwf | 14 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 83 |
| open-meteo-gfs | 14 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 84 |
| persistence | 15 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 84 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
