# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (139 days on file, through 2026-11-19) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.9 | 2.8 | 3.4 | 4.0 | 4.2 | 5.0 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 3.0 | 3.4 | 4.0 | 4.2 | 5.3 | 5.4 | 6.0 | 8.6 |
| open-meteo-gfs | 2.7 | 3.7 | 3.4 | 3.8 | 3.2 | 4.7 | 6.2 | 6.2 | 8.5 |
| persistence | 5.7 | 7.9 | 9.1 | 9.7 | 8.9 | 8.0 | 7.0 | 8.2 | 9.4 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.7 | -2.7 | -2.9 | -2.8 | -2.9 | -2.9 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.9 | -3.1 | -3.6 | -3.4 | -3.5 | -3.7 | -4.0 | -5.6 |
| open-meteo-gfs | -2.6 | -3.5 | -3.2 | -3.7 | -3.0 | -4.5 | -5.1 | -5.2 | -6.7 |
| persistence | 1.8 | 0.9 | 1.3 | 2.1 | 2.5 | 3.0 | 3.7 | 4.1 | 4.7 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.4 | 3.4 | 3.3 | 3.6 | 4.4 | 5.4 | 6.0 | — |
| open-meteo-ecmwf | 4.2 | 4.9 | 5.2 | 5.3 | 5.2 | 5.1 | 5.6 | 6.4 | 6.9 |
| open-meteo-gfs | 3.1 | 4.2 | 4.0 | 4.6 | 4.7 | 5.1 | 6.0 | 5.6 | 8.3 |
| persistence | 4.3 | 6.6 | 8.7 | 9.5 | 9.1 | 8.8 | 8.5 | 8.8 | 10.6 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.057 | 0.063 | 0.043 | 0.023 | 0.038 | 0.053 | 0.071 | 0.000* | — |
| open-meteo-ecmwf | 0.016 | 0.045 | 0.046 | 0.027 | 0.029 | 0.046 | 0.058 | 0.080 | 0.130 |
| open-meteo-gfs | 0.074 | 0.067 | 0.053 | 0.028 | 0.033 | 0.043 | 0.058 | 0.070 | 0.097 |
| persistence | 0.158 | 0.278 | 0.314 | 0.294 | 0.273 | 0.219 | 0.226 | 0.267 | 0.291 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 92 | 94 | 97 | 97 | 91 | 90 | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 94 | 97 | 94 | 91 | 87 | 93 | 86 |
| open-meteo-gfs | 83 | 89 | 91 | 94 | 94 | 88 | 94 | 90 | 88 |
| persistence | 84 | 72 | 69 | 71 | 73 | 78 | 77 | 73 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.09 | 0.03 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.00 | 0.04 | 0.10 | 0.13 | 0.10 |
| persistence | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 19 | 36 | 35 | 34 | 33 | 32 | 31 | 1 | 0 |
| open-meteo-ecmwf | 18 | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 168 |
| open-meteo-gfs | 18 | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 182 |
| persistence | 19 | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 182 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
