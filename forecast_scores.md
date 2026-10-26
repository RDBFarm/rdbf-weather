# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (114 days on file, through 2026-10-25) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.9 | 4.2 | 4.3 | 5.2* | 4.5* | 4.0* | 3.8* | 1.0* | — |
| open-meteo-ecmwf | 3.2* | 3.4 | 3.5 | 4.6* | 5.0* | 5.2* | 5.9* | 5.5* | 6.3 |
| open-meteo-gfs | 2.6* | 3.3 | 3.9 | 4.3* | 3.1* | 4.0* | 4.1* | 2.4* | 5.2 |
| persistence | 5.6 | 6.9 | 7.6 | 9.2* | 9.0* | 8.3* | 10.7* | 13.6* | 16.9 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.7 | -4.2 | -4.3 | -5.2* | -4.5* | -4.0* | -3.2* | -1.0* | — |
| open-meteo-ecmwf | -3.0* | -3.1 | -3.5 | -4.6* | -5.0* | -5.2* | -5.9* | -5.2* | -6.2 |
| open-meteo-gfs | -2.5* | -3.1 | -3.4 | -4.3* | -3.1* | -4.0* | -4.1* | -0.9* | -2.5 |
| persistence | 2.8 | 3.6 | 5.0 | 7.0* | 7.2* | 7.1* | 8.3* | 11.6* | 16.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.4 | 3.2* | 3.1* | 3.9* | 5.7* | 7.4* | — |
| open-meteo-ecmwf | 4.0* | 4.2 | 4.6 | 4.8* | 4.0* | 3.6* | 5.4* | 6.6* | 7.7 |
| open-meteo-gfs | 3.1* | 3.2 | 3.0 | 3.0* | 3.1* | 3.1* | 4.5* | 4.4* | 6.4 |
| persistence | 3.9 | 5.7 | 8.3 | 9.7* | 10.4* | 11.6* | 12.8* | 15.4* | 18.2 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.108 | 0.084 | 0.079 | 0.039* | 0.004* | 0.003* | 0.003* | 0.000* | — |
| open-meteo-ecmwf | 0.031* | 0.036 | 0.043 | 0.027* | 0.009* | 0.013* | 0.011* | 0.021* | 0.117 |
| open-meteo-gfs | 0.147* | 0.107 | 0.061 | 0.047* | 0.003* | 0.003* | 0.002* | 0.002* | 0.009 |
| persistence | 0.200 | 0.364 | 0.500 | 0.444* | 0.375* | 0.429* | 0.500* | 0.600* | 0.300 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 80 | 91 | 90 | 89* | 100* | 100* | 100* | 100* | — |
| open-meteo-ecmwf | 100* | 91 | 90 | 100* | 100* | 100* | 100* | 100* | 90 |
| open-meteo-gfs | 67* | 82 | 90 | 89* | 100* | 100* | 100* | 100* | 100 |
| persistence | 80 | 64 | 50 | 56* | 62* | 57* | 50* | 40* | 70 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02* | 0.02 | 0.00 | 0.00* | 0.00* | 0.00* | 0.00* | 0.00* | 0.02 |
| open-meteo-gfs | 0.02* | 0.02 | 0.01 | 0.01* | 0.00* | 0.00* | 0.00* | 0.00* | 0.00 |
| persistence | 0.03 | 0.06 | 0.05 | 0.04* | 0.04* | 0.05* | 0.05* | 0.06* | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 10 | 11 | 10 | 9 | 8 | 7 | 6 | 1 | 0 |
| open-meteo-ecmwf | 9 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 10 |
| open-meteo-gfs | 9 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 10 |
| persistence | 10 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 10 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
