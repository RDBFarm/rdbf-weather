# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (105 days on file, through 2026-10-16) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 6.0* | 5.5* | 1.0* | — | — | — | — | — | — |
| open-meteo-ecmwf | 1.7* | 2.0* | 0.4* | — | — | — | — | — | — |
| open-meteo-gfs | 0.8* | 0.8* | 2.8* | — | — | — | — | — | — |
| persistence | 11.0* | 8.5* | 2.0* | — | — | — | — | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -5.0* | -5.5* | -1.0* | — | — | — | — | — | — |
| open-meteo-ecmwf | -1.7* | -1.0* | -0.4* | — | — | — | — | — | — |
| open-meteo-gfs | -0.3* | 0.0* | 2.8* | — | — | — | — | — | — |
| persistence | 4.0* | 8.5* | 2.0* | — | — | — | — | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 1.0* | 3.0* | — | — | — | — | — | — |
| open-meteo-ecmwf | 1.4* | 2.4* | 1.2* | — | — | — | — | — | — |
| open-meteo-gfs | 1.7* | 0.7* | 3.3* | — | — | — | — | — | — |
| persistence | 2.0* | 3.5* | 9.0* | — | — | — | — | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.177* | 0.150* | 0.144* | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.126* | 0.068* | 0.152* | — | — | — | — | — | — |
| open-meteo-gfs | 0.495* | 0.226* | 0.397* | — | — | — | — | — | — |
| persistence | 0.500* | 1.000* | 1.000* | — | — | — | — | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 50* | 100* | 100* | — | — | — | — | — | — |
| open-meteo-ecmwf | 100* | 100* | 100* | — | — | — | — | — | — |
| open-meteo-gfs | 0* | 50* | 0* | — | — | — | — | — | — |
| persistence | 50* | 0* | 0* | — | — | — | — | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.09* | 0.09* | 0.03* | — | — | — | — | — | — |
| open-meteo-gfs | 0.09* | 0.11* | 0.09* | — | — | — | — | — | — |
| persistence | 0.09* | 0.16* | 0.17* | — | — | — | — | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-ecmwf | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-gfs | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| persistence | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
