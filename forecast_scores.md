# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (137 days on file, through 2026-11-17) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.7 | 2.6 | 3.2 | 3.9 | 4.0 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.3 | 3.9 | 4.1 | 5.2 | 5.2 | 5.7 | 8.2 |
| open-meteo-gfs | 2.7 | 3.6 | 3.3 | 3.6 | 3.0 | 4.4 | 5.9 | 5.7 | 8.2 |
| persistence | 5.7 | 7.7 | 8.8 | 9.2 | 8.2 | 7.7 | 7.1 | 8.5 | 9.6 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.4 | -2.5 | -2.8 | -2.6 | -2.7 | -2.5 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.8 | -3.0 | -3.4 | -3.2 | -3.2 | -3.4 | -3.4 | -5.1 |
| open-meteo-gfs | -2.6 | -3.5 | -3.0 | -3.5 | -2.8 | -4.2 | -4.7 | -4.6 | -6.3 |
| persistence | 1.8 | 1.6 | 2.3 | 3.4 | 3.9 | 4.0 | 4.2 | 4.3 | 5.1 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.2 | 3.2 | 3.1 | 3.5 | 4.5 | 5.6 | 6.2 | — |
| open-meteo-ecmwf | 4.2 | 4.7 | 5.0 | 5.0 | 5.0 | 4.8 | 5.4 | 6.3 | 6.8 |
| open-meteo-gfs | 3.1 | 3.9 | 3.6 | 4.2 | 4.4 | 4.8 | 5.9 | 5.5 | 8.2 |
| persistence | 4.3 | 6.9 | 8.9 | 9.4 | 8.7 | 8.2 | 8.1 | 8.8 | 9.8 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.057 | 0.067 | 0.046 | 0.024 | 0.040 | 0.057 | 0.076 | 0.000* | — |
| open-meteo-ecmwf | 0.016 | 0.048 | 0.049 | 0.028 | 0.031 | 0.049 | 0.062 | 0.086 | 0.141 |
| open-meteo-gfs | 0.074 | 0.071 | 0.056 | 0.030 | 0.036 | 0.046 | 0.062 | 0.075 | 0.105 |
| persistence | 0.158 | 0.294 | 0.333 | 0.312 | 0.290 | 0.200 | 0.207 | 0.286 | 0.292 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 91 | 94 | 97 | 97 | 90 | 90 | 100* | — |
| open-meteo-ecmwf | 100 | 91 | 94 | 97 | 94 | 90 | 86 | 93 | 85 |
| open-meteo-gfs | 83 | 88 | 91 | 94 | 94 | 87 | 93 | 89 | 88 |
| persistence | 84 | 71 | 67 | 69 | 71 | 80 | 79 | 71 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.09 | 0.03 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.05 | 0.11 | 0.14 | 0.11 |
| persistence | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 19 | 34 | 33 | 32 | 31 | 30 | 29 | 1 | 0 |
| open-meteo-ecmwf | 18 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 156 |
| open-meteo-gfs | 18 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 168 |
| persistence | 19 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 168 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
