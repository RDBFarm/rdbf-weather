# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (138 days on file, through 2026-11-18) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.8 | 2.6 | 3.2 | 3.9 | 4.1 | 4.8 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.3 | 3.9 | 4.2 | 5.2 | 5.3 | 5.9 | 8.4 |
| open-meteo-gfs | 2.7 | 3.6 | 3.3 | 3.6 | 3.1 | 4.5 | 6.0 | 5.9 | 8.3 |
| persistence | 5.7 | 7.7 | 8.9 | 9.4 | 8.4 | 7.6 | 6.9 | 8.4 | 9.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.5 | -2.5 | -2.8 | -2.7 | -2.8 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.8 | -3.0 | -3.5 | -3.3 | -3.3 | -3.5 | -3.8 | -5.3 |
| open-meteo-gfs | -2.6 | -3.5 | -3.1 | -3.5 | -2.9 | -4.3 | -4.9 | -4.9 | -6.5 |
| persistence | 1.8 | 1.3 | 1.8 | 2.8 | 3.2 | 3.8 | 4.1 | 4.3 | 5.0 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.3 | 3.3 | 3.2 | 3.6 | 4.4 | 5.5 | 6.1 | — |
| open-meteo-ecmwf | 4.2 | 4.8 | 5.2 | 5.2 | 5.1 | 5.0 | 5.6 | 6.3 | 6.9 |
| open-meteo-gfs | 3.1 | 4.0 | 3.8 | 4.4 | 4.5 | 5.0 | 5.9 | 5.5 | 8.3 |
| persistence | 4.3 | 6.8 | 8.9 | 9.6 | 8.9 | 8.5 | 8.2 | 8.8 | 10.2 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.057 | 0.065 | 0.045 | 0.024 | 0.039 | 0.055 | 0.073 | 0.000* | — |
| open-meteo-ecmwf | 0.016 | 0.047 | 0.048 | 0.027 | 0.030 | 0.047 | 0.060 | 0.083 | 0.135 |
| open-meteo-gfs | 0.074 | 0.069 | 0.054 | 0.029 | 0.034 | 0.045 | 0.060 | 0.072 | 0.101 |
| persistence | 0.158 | 0.286 | 0.324 | 0.303 | 0.281 | 0.226 | 0.200 | 0.276 | 0.291 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 91 | 94 | 97 | 97 | 90 | 90 | 100* | — |
| open-meteo-ecmwf | 100 | 91 | 94 | 97 | 94 | 90 | 87 | 93 | 85 |
| open-meteo-gfs | 83 | 89 | 91 | 94 | 94 | 87 | 93 | 90 | 88 |
| persistence | 84 | 71 | 68 | 70 | 72 | 77 | 80 | 72 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.09 | 0.03 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.10 | 0.14 | 0.10 |
| persistence | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 19 | 35 | 34 | 33 | 32 | 31 | 30 | 1 | 0 |
| open-meteo-ecmwf | 18 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 162 |
| open-meteo-gfs | 18 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 175 |
| persistence | 19 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 175 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
