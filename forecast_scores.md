# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (145 days on file, through 2026-11-25) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 2.9 | 2.9 | 2.8 | 3.3 | 3.8 | 3.9 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.0 | 2.9 | 3.4 | 3.8 | 4.1 | 5.0 | 5.1 | 5.8 | 8.1 |
| open-meteo-gfs | 2.7 | 3.6 | 3.6 | 3.8 | 3.5 | 4.9 | 6.0 | 6.4 | 8.4 |
| persistence | 6.1 | 8.1 | 9.1 | 9.8 | 9.5 | 9.2 | 8.2 | 8.9 | 9.0 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.8 | -2.3 | -2.3 | -2.6 | -2.6 | -2.7 | -2.7 | -1.0* | — |
| open-meteo-ecmwf | -2.9 | -2.5 | -2.8 | -3.2 | -3.2 | -3.2 | -3.4 | -3.5 | -4.6 |
| open-meteo-gfs | -2.7 | -3.2 | -3.2 | -3.6 | -3.0 | -4.6 | -5.0 | -5.6 | -6.3 |
| persistence | 2.6 | 1.8 | 2.0 | 2.5 | 2.5 | 2.4 | 2.4 | 2.5 | 4.2 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 8.0* | 3.5 | 3.4 | 3.5 | 3.8 | 4.4 | 5.2 | 5.8 | — |
| open-meteo-ecmwf | 4.6 | 5.0 | 5.2 | 5.2 | 5.3 | 5.2 | 5.7 | 6.5 | 7.0 |
| open-meteo-gfs | 3.3 | 4.3 | 4.0 | 4.7 | 5.0 | 5.3 | 5.6 | 5.8 | 8.2 |
| persistence | 4.9 | 7.7 | 9.4 | 9.7 | 9.1 | 8.8 | 8.5 | 8.7 | 10.5 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.052 | 0.078 | 0.060 | 0.041 | 0.041 | 0.058 | 0.070 | 0.000* | — |
| open-meteo-ecmwf | 0.014 | 0.045 | 0.050 | 0.037 | 0.036 | 0.049 | 0.057 | 0.070 | 0.126 |
| open-meteo-gfs | 0.066 | 0.064 | 0.059 | 0.046 | 0.039 | 0.043 | 0.056 | 0.059 | 0.085 |
| persistence | 0.143 | 0.238 | 0.268 | 0.250 | 0.231 | 0.184 | 0.189 | 0.250 | 0.272 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 90 | 88 | 90 | 92 | 97 | 89 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 95 | 95 | 92 | 92 | 89 | 94 | 87 |
| open-meteo-gfs | 85 | 88 | 90 | 92 | 92 | 89 | 95 | 92 | 91 |
| persistence | 86 | 76 | 73 | 75 | 77 | 82 | 81 | 75 | 73 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.06 | 0.06 | 0.12 | 0.08 | 0.03 | 0.10 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.06 | 0.05 | 0.07 | 0.09 | 0.11 | 0.09 |
| persistence | 0.02 | 0.02 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 21 | 42 | 41 | 40 | 39 | 38 | 37 | 1 | 0 |
| open-meteo-ecmwf | 20 | 42 | 41 | 40 | 39 | 38 | 37 | 36 | 205 |
| open-meteo-gfs | 20 | 42 | 41 | 40 | 39 | 38 | 37 | 36 | 224 |
| persistence | 21 | 42 | 41 | 40 | 39 | 38 | 37 | 36 | 224 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
