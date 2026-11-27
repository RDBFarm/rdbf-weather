# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (146 days on file, through 2026-11-26) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 2.9 | 2.9 | 2.9 | 3.3 | 3.8 | 3.9 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.0 | 2.9 | 3.4 | 3.8 | 4.0 | 5.1 | 5.1 | 6.0 | 8.0 |
| open-meteo-gfs | 2.7 | 3.6 | 3.6 | 3.8 | 3.6 | 5.0 | 6.0 | 6.3 | 8.3 |
| persistence | 6.1 | 8.0 | 9.3 | 9.9 | 9.5 | 9.4 | 8.5 | 9.0 | 8.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.8 | -2.2 | -2.1 | -2.4 | -2.6 | -2.7 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -2.9 | -2.5 | -2.9 | -3.1 | -3.2 | -3.3 | -3.3 | -3.8 | -4.5 |
| open-meteo-gfs | -2.7 | -3.0 | -3.0 | -3.5 | -2.8 | -4.3 | -4.9 | -5.5 | -6.2 |
| persistence | 2.6 | 1.7 | 2.3 | 2.7 | 2.7 | 2.7 | 2.8 | 2.8 | 4.2 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 8.0* | 3.4 | 3.4 | 3.4 | 3.8 | 4.4 | 5.2 | 5.8 | — |
| open-meteo-ecmwf | 4.6 | 4.9 | 5.1 | 5.1 | 5.1 | 5.1 | 5.6 | 6.5 | 6.9 |
| open-meteo-gfs | 3.3 | 4.2 | 4.0 | 4.7 | 5.0 | 5.2 | 5.7 | 5.7 | 8.3 |
| persistence | 4.9 | 7.8 | 9.3 | 9.6 | 9.0 | 8.8 | 8.6 | 8.8 | 10.4 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.052 | 0.076 | 0.058 | 0.040 | 0.041 | 0.061 | 0.073 | 0.000* | — |
| open-meteo-ecmwf | 0.014 | 0.044 | 0.049 | 0.037 | 0.035 | 0.049 | 0.060 | 0.071 | 0.136 |
| open-meteo-gfs | 0.066 | 0.062 | 0.057 | 0.045 | 0.039 | 0.044 | 0.061 | 0.061 | 0.098 |
| persistence | 0.143 | 0.256 | 0.286 | 0.268 | 0.250 | 0.205 | 0.211 | 0.270 | 0.290 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 88 | 90 | 93 | 98 | 90 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 95 | 95 | 92 | 92 | 89 | 95 | 85 |
| open-meteo-gfs | 85 | 88 | 90 | 93 | 92 | 90 | 95 | 92 | 88 |
| persistence | 86 | 74 | 71 | 73 | 75 | 79 | 79 | 73 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.03 | 0.03 | 0.06 | 0.09 | 0.13 | 0.13 | 0.04 | 0.15 |
| open-meteo-gfs | 0.01 | 0.02 | 0.02 | 0.08 | 0.07 | 0.08 | 0.14 | 0.15 | 0.13 |
| persistence | 0.02 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.07 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 21 | 43 | 42 | 41 | 40 | 39 | 38 | 1 | 0 |
| open-meteo-ecmwf | 20 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 211 |
| open-meteo-gfs | 20 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 231 |
| persistence | 21 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 231 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
