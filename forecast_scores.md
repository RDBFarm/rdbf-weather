# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (117 days on file, through 2026-10-28) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4.1 | 4.0 | 4.1 | 4.9 | 4.7 | 4.1 | 3.8* | 1.0* | — |
| open-meteo-ecmwf | 3.5 | 3.6 | 3.8 | 4.7 | 5.3 | 6.1 | 5.8* | 5.2* | 6.7 |
| open-meteo-gfs | 2.8 | 3.3 | 4.0 | 4.5 | 3.5 | 4.4 | 5.2* | 3.0* | 5.7 |
| persistence | 5.3 | 6.9 | 7.2 | 8.2 | 7.7 | 6.8 | 7.9* | 10.9* | 12.3 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.9 | -4.0 | -4.1 | -4.9 | -4.7 | -4.1 | -3.3* | -1.0* | — |
| open-meteo-ecmwf | -3.4 | -3.4 | -3.8 | -4.7 | -5.3 | -6.1 | -5.8* | -4.6* | -6.7 |
| open-meteo-gfs | -2.7 | -3.2 | -3.6 | -4.5 | -3.5 | -4.4 | -5.2* | -2.0* | -3.9 |
| persistence | 2.4 | 2.3 | 2.6 | 4.0 | 4.1 | 4.4 | 5.0* | 6.1* | 9.5 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.6 | 2.9 | 2.8 | 2.9 | 3.3 | 4.9* | 6.2* | — |
| open-meteo-ecmwf | 4.2 | 4.3 | 4.7 | 4.7 | 4.0 | 3.6 | 4.2* | 5.5* | 5.3 |
| open-meteo-gfs | 3.2 | 3.5 | 3.2 | 3.1 | 3.3 | 3.8 | 4.2* | 4.5* | 7.4 |
| persistence | 4.3 | 5.6 | 7.8 | 8.5 | 8.8 | 9.6 | 9.8* | 11.5* | 14.5 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.098 | 0.066 | 0.061 | 0.029 | 0.003 | 0.002 | 0.002* | 0.000* | — |
| open-meteo-ecmwf | 0.028 | 0.028 | 0.033 | 0.020 | 0.007 | 0.009 | 0.008* | 0.013* | 0.051 |
| open-meteo-gfs | 0.133 | 0.084 | 0.047 | 0.035 | 0.002 | 0.002 | 0.001* | 0.002* | 0.013 |
| persistence | 0.182 | 0.286 | 0.385 | 0.333 | 0.273 | 0.300 | 0.333* | 0.375* | 0.429 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 82 | 93 | 92 | 92 | 100 | 100 | 100* | 100* | — |
| open-meteo-ecmwf | 100 | 93 | 92 | 100 | 100 | 100 | 100* | 100* | 96 |
| open-meteo-gfs | 70 | 86 | 92 | 92 | 100 | 100 | 100* | 100* | 100 |
| persistence | 82 | 71 | 62 | 67 | 73 | 70 | 67* | 62* | 57 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00* | 0.00* | 0.02 |
| open-meteo-gfs | 0.02 | 0.02 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00* | 0.00* | 0.03 |
| persistence | 0.03 | 0.04 | 0.04 | 0.03 | 0.03 | 0.03 | 0.04* | 0.04* | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 11 | 14 | 13 | 12 | 11 | 10 | 9 | 1 | 0 |
| open-meteo-ecmwf | 10 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 28 |
| open-meteo-gfs | 10 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 28 |
| persistence | 11 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 28 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
