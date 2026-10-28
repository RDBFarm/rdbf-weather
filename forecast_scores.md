# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (116 days on file, through 2026-10-27) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4.1 | 4.3 | 4.4 | 5.3 | 4.9 | 4.2* | 4.2* | 1.0* | — |
| open-meteo-ecmwf | 3.5 | 3.8 | 4.1 | 5.1 | 5.6 | 6.2* | 5.9* | 5.7* | 7.0 |
| open-meteo-gfs | 2.8 | 3.5 | 4.3 | 4.7 | 3.5 | 4.5* | 5.3* | 2.8* | 6.0 |
| persistence | 5.3 | 6.9 | 7.8 | 8.8 | 8.3 | 7.3* | 8.8* | 11.7* | 13.0 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.9 | -4.3 | -4.4 | -5.3 | -4.9 | -4.2* | -3.8* | -1.0* | — |
| open-meteo-ecmwf | -3.4 | -3.6 | -4.1 | -5.1 | -5.6 | -6.2* | -5.9* | -5.5* | -7.0 |
| open-meteo-gfs | -2.7 | -3.4 | -3.8 | -4.7 | -3.5 | -4.5* | -5.3* | -1.7* | -4.7 |
| persistence | 2.4 | 2.0 | 2.8 | 4.5 | 4.7 | 4.7* | 5.5* | 6.3* | 9.8 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.7 | 3.1 | 3.0 | 3.1 | 3.7* | 5.4* | 7.0* | — |
| open-meteo-ecmwf | 4.2 | 4.4 | 4.8 | 4.9 | 4.3 | 4.0* | 4.5* | 5.6* | 6.0 |
| open-meteo-gfs | 3.2 | 3.4 | 3.3 | 3.4 | 3.5 | 3.7* | 4.5* | 4.8* | 7.5 |
| persistence | 4.3 | 5.3 | 7.9 | 8.5 | 9.2 | 9.9* | 10.2* | 12.3* | 16.0 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.098 | 0.071 | 0.066 | 0.032 | 0.003 | 0.002* | 0.002* | 0.000* | — |
| open-meteo-ecmwf | 0.028 | 0.030 | 0.036 | 0.022 | 0.007 | 0.010* | 0.009* | 0.015* | 0.064 |
| open-meteo-gfs | 0.133 | 0.090 | 0.051 | 0.038 | 0.002 | 0.002* | 0.001* | 0.002* | 0.013 |
| persistence | 0.182 | 0.308 | 0.417 | 0.364 | 0.300 | 0.333* | 0.375* | 0.429* | 0.429 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 82 | 92 | 92 | 91 | 100 | 100* | 100* | 100* | — |
| open-meteo-ecmwf | 100 | 92 | 92 | 100 | 100 | 100* | 100* | 100* | 95 |
| open-meteo-gfs | 70 | 85 | 92 | 91 | 100 | 100* | 100* | 100* | 100 |
| persistence | 82 | 69 | 58 | 64 | 70 | 67* | 62* | 57* | 57 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00* | 0.00* | 0.00* | 0.02 |
| open-meteo-gfs | 0.02 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00* | 0.00* | 0.00* | 0.01 |
| persistence | 0.03 | 0.05 | 0.04 | 0.03 | 0.03 | 0.04* | 0.04* | 0.05* | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 11 | 13 | 12 | 11 | 10 | 9 | 8 | 1 | 0 |
| open-meteo-ecmwf | 10 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 21 |
| open-meteo-gfs | 10 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 21 |
| persistence | 11 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 21 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
