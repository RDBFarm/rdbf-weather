# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (118 days on file, through 2026-10-29) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4.2 | 4.1 | 4.1 | 5.0 | 4.8 | 4.4 | 4.4 | 1.0* | — |
| open-meteo-ecmwf | 3.7 | 3.7 | 4.0 | 4.8 | 5.3 | 6.2 | 5.6 | 5.8* | 8.3 |
| open-meteo-gfs | 3.3 | 3.4 | 4.0 | 4.6 | 3.8 | 4.9 | 5.5 | 3.8* | 7.1 |
| persistence | 5.7 | 6.5 | 7.0 | 8.2 | 8.0 | 7.3 | 7.9 | 10.7* | 11.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -4.0 | -4.1 | -4.1 | -5.0 | -4.8 | -4.4 | -4.0 | -1.0* | — |
| open-meteo-ecmwf | -3.6 | -3.5 | -4.0 | -4.8 | -5.3 | -6.2 | -5.6 | -5.2* | -8.2 |
| open-meteo-gfs | -3.2 | -3.3 | -3.6 | -4.6 | -3.8 | -4.9 | -5.5 | -3.0* | -5.7 |
| persistence | 1.3 | 2.0 | 2.1 | 3.0 | 2.8 | 2.9 | 3.7 | 4.4* | 6.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.7 | 2.9 | 2.8 | 2.8 | 3.2 | 4.5 | 5.8* | — |
| open-meteo-ecmwf | 4.2 | 4.2 | 4.6 | 4.7 | 4.0 | 3.4 | 4.3 | 4.9* | 5.0 |
| open-meteo-gfs | 3.3 | 3.4 | 3.2 | 3.2 | 3.2 | 3.5 | 4.5 | 4.0* | 7.5 |
| persistence | 3.9 | 5.3 | 7.9 | 8.4 | 8.8 | 9.2 | 9.5 | 10.9* | 13.7 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.090 | 0.062 | 0.056 | 0.027 | 0.003 | 0.002 | 0.002 | 0.000* | — |
| open-meteo-ecmwf | 0.025 | 0.026 | 0.031 | 0.019 | 0.006 | 0.009 | 0.007 | 0.012* | 0.044 |
| open-meteo-gfs | 0.121 | 0.078 | 0.044 | 0.033 | 0.002 | 0.002 | 0.001 | 0.001* | 0.012 |
| persistence | 0.167 | 0.267 | 0.357 | 0.308 | 0.250 | 0.273 | 0.300 | 0.333* | 0.429 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 83 | 93 | 93 | 92 | 100 | 100 | 100 | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 93 | 100 | 100 | 100 | 100 | 100* | 97 |
| open-meteo-gfs | 73 | 87 | 93 | 92 | 100 | 100 | 100 | 100* | 100 |
| persistence | 83 | 73 | 64 | 69 | 75 | 73 | 70 | 67* | 57 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00* | 0.03 |
| open-meteo-gfs | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00* | 0.04 |
| persistence | 0.03 | 0.04 | 0.04 | 0.03 | 0.03 | 0.03 | 0.03 | 0.04* | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 12 | 15 | 14 | 13 | 12 | 11 | 10 | 1 | 0 |
| open-meteo-ecmwf | 11 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 35 |
| open-meteo-gfs | 11 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 35 |
| persistence | 12 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 35 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
