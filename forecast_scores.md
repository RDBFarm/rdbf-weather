# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (106 days on file, through 2026-10-17) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 6.3* | 6.3* | 4.5* | 8.0* | — | — | — | — | — |
| open-meteo-ecmwf | 1.4* | 1.5* | 0.7* | 1.9* | — | — | — | — | — |
| open-meteo-gfs | 1.5* | 1.4* | 3.4* | 7.7* | — | — | — | — | — |
| persistence | 13.7* | 9.7* | 14.5* | 21.0* | — | — | — | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -5.7* | -6.3* | -4.5* | -8.0* | — | — | — | — | — |
| open-meteo-ecmwf | -0.9* | -0.5* | -0.7* | -1.9* | — | — | — | — | — |
| open-meteo-gfs | -1.2* | -0.9* | -0.7* | -7.7* | — | — | — | — | — |
| persistence | 9.0* | 9.7* | 14.5* | 21.0* | — | — | — | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.7* | 7.0* | 10.0* | — | — | — | — | — |
| open-meteo-ecmwf | 3.6* | 3.8* | 4.8* | 8.2* | — | — | — | — | — |
| open-meteo-gfs | 2.5* | 1.1* | 1.8* | 1.5* | — | — | — | — | — |
| persistence | 8.3* | 8.7* | 15.0* | 12.0* | — | — | — | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.359* | 0.308* | 0.392* | 0.325* | — | — | — | — | — |
| open-meteo-ecmwf | 0.093* | 0.132* | 0.217* | 0.240* | — | — | — | — | — |
| open-meteo-gfs | 0.442* | 0.391* | 0.304* | 0.397* | — | — | — | — | — |
| persistence | 0.333* | 0.667* | 1.000* | 1.000* | — | — | — | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 33* | 67* | 50* | 0* | — | — | — | — | — |
| open-meteo-ecmwf | 100* | 67* | 50* | 100* | — | — | — | — | — |
| open-meteo-gfs | 0* | 33* | 50* | 0* | — | — | — | — | — |
| persistence | 67* | 33* | 0* | 0* | — | — | — | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.07* | 0.06* | 0.01* | 0.03* | — | — | — | — | — |
| open-meteo-gfs | 0.06* | 0.07* | 0.05* | 0.06* | — | — | — | — | — |
| persistence | 0.11* | 0.15* | 0.09* | 0.01* | — | — | — | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-ecmwf | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-gfs | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| persistence | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
