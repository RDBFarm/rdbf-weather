# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (107 days on file, through 2026-10-18) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 5.8* | 6.0* | 5.3* | 7.5* | 6.0* | — | — | — | — |
| open-meteo-ecmwf | 2.2* | 2.2* | 2.4* | 3.2* | 6.2* | — | — | — | — |
| open-meteo-gfs | 2.4* | 2.4* | 4.8* | 6.1* | 4.0* | — | — | — | — |
| persistence | 10.5* | 11.8* | 13.3* | 23.5* | 20.0* | — | — | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -5.2* | -6.0* | -5.3* | -7.5* | -6.0* | — | — | — | — |
| open-meteo-ecmwf | -1.8* | -1.4* | -2.4* | -3.2* | -6.2* | — | — | — | — |
| open-meteo-gfs | -2.2* | -2.1* | -2.9* | -6.1* | -4.0* | — | — | — | — |
| persistence | 6.5* | 11.8* | 13.3* | 23.5* | 20.0* | — | — | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.2* | 5.0* | 5.0* | 1.0* | — | — | — | — |
| open-meteo-ecmwf | 3.4* | 3.7* | 4.6* | 6.1* | 3.5* | — | — | — | — |
| open-meteo-gfs | 2.2* | 1.0* | 1.8* | 1.4* | 1.3* | — | — | — | — |
| persistence | 6.8* | 12.2* | 17.0* | 17.5* | 14.0* | — | — | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.269* | 0.231* | 0.263* | 0.171* | 0.002* | — | — | — | — |
| open-meteo-ecmwf | 0.070* | 0.099* | 0.144* | 0.120* | 0.062* | — | — | — | — |
| open-meteo-gfs | 0.332* | 0.294* | 0.203* | 0.202* | 0.000* | — | — | — | — |
| persistence | 0.500* | 0.750* | 1.000* | 0.500* | 0.000* | — | — | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 50* | 75* | 67* | 50* | 100* | — | — | — | — |
| open-meteo-ecmwf | 100* | 75* | 67* | 100* | 100* | — | — | — | — |
| open-meteo-gfs | 25* | 50* | 67* | 50* | 100* | — | — | — | — |
| persistence | 50* | 25* | 0* | 50* | 100* | — | — | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.06* | 0.05* | 0.01* | 0.01* | 0.00* | — | — | — | — |
| open-meteo-gfs | 0.05* | 0.06* | 0.03* | 0.03* | 0.00* | — | — | — | — |
| persistence | 0.09* | 0.15* | 0.11* | 0.01* | 0.00* | — | — | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| open-meteo-ecmwf | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| open-meteo-gfs | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| persistence | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
