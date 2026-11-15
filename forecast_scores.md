# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (134 days on file, through 2026-11-14) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.1 | 2.9 | 2.9 | 3.4 | 3.9 | 4.0 | 4.8 | 1.0* | — |
| open-meteo-ecmwf | 3.2 | 3.0 | 3.4 | 3.9 | 4.1 | 5.3 | 5.0 | 5.3 | 8.5 |
| open-meteo-gfs | 2.7 | 3.6 | 3.2 | 3.5 | 2.9 | 4.2 | 5.9 | 5.7 | 8.6 |
| persistence | 5.9 | 7.8 | 8.7 | 9.0 | 7.8 | 7.3 | 6.8 | 8.9 | 9.0 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.0 | -2.6 | -2.7 | -2.9 | -2.6 | -2.6 | -2.3 | -1.0* | — |
| open-meteo-ecmwf | -3.1 | -2.8 | -3.1 | -3.5 | -3.2 | -3.1 | -2.9 | -2.8 | -5.8 |
| open-meteo-gfs | -2.6 | -3.4 | -2.9 | -3.4 | -2.7 | -4.0 | -4.6 | -4.5 | -6.7 |
| persistence | 2.1 | 2.4 | 2.8 | 3.3 | 3.1 | 3.2 | 3.6 | 4.2 | 3.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.1 | 3.2 | 3.7 | 4.7 | 5.9 | 6.7 | — |
| open-meteo-ecmwf | 4.0 | 4.2 | 4.6 | 4.7 | 4.8 | 4.8 | 5.7 | 6.5 | 6.3 |
| open-meteo-gfs | 3.1 | 3.9 | 3.6 | 4.2 | 4.4 | 5.0 | 6.0 | 5.7 | 8.4 |
| persistence | 4.1 | 6.7 | 8.5 | 9.2 | 8.6 | 8.4 | 8.2 | 8.5 | 8.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.060 | 0.073 | 0.051 | 0.027 | 0.045 | 0.063 | 0.085 | 0.000* | — |
| open-meteo-ecmwf | 0.017 | 0.053 | 0.054 | 0.031 | 0.035 | 0.054 | 0.070 | 0.096 | 0.146 |
| open-meteo-gfs | 0.078 | 0.077 | 0.061 | 0.033 | 0.039 | 0.052 | 0.069 | 0.084 | 0.118 |
| persistence | 0.167 | 0.323 | 0.333 | 0.310 | 0.286 | 0.222 | 0.231 | 0.320 | 0.293 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 90 | 93 | 97 | 96 | 89 | 88 | 100* | — |
| open-meteo-ecmwf | 100 | 90 | 93 | 97 | 93 | 89 | 85 | 92 | 84 |
| open-meteo-gfs | 82 | 87 | 90 | 93 | 93 | 85 | 92 | 88 | 86 |
| persistence | 83 | 68 | 67 | 69 | 71 | 78 | 77 | 68 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.04 | 0.02 | 0.01 | 0.11 | 0.04 | 0.10 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.05 | 0.12 | 0.16 | 0.12 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 18 | 31 | 30 | 29 | 28 | 27 | 26 | 1 | 0 |
| open-meteo-ecmwf | 17 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 137 |
| open-meteo-gfs | 17 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 147 |
| persistence | 18 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 147 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
