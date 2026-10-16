# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (104 days on file, through 2026-10-15) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 11.0* | 11.0* | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 2.9* | 3.1* | — | — | — | — | — | — | — |
| open-meteo-gfs | 0.5* | 0.8* | — | — | — | — | — | — | — |
| persistence | 15.0* | 9.0* | — | — | — | — | — | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -11.0* | -11.0* | — | — | — | — | — | — | — |
| open-meteo-ecmwf | -2.9* | -3.1* | — | — | — | — | — | — | — |
| open-meteo-gfs | 0.5* | -0.8* | — | — | — | — | — | — | — |
| persistence | 15.0* | 9.0* | — | — | — | — | — | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 0.0* | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 2.8* | 2.5* | — | — | — | — | — | — | — |
| open-meteo-gfs | 3.2* | 0.2* | — | — | — | — | — | — | — |
| persistence | 2.0* | 7.0* | — | — | — | — | — | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.281* | 0.116* | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.212* | 0.078* | — | — | — | — | — | — | — |
| open-meteo-gfs | 0.593* | 0.160* | — | — | — | — | — | — | — |
| persistence | 1.000* | 1.000* | — | — | — | — | — | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0* | 100* | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 100* | 100* | — | — | — | — | — | — | — |
| open-meteo-gfs | 0* | 100* | — | — | — | — | — | — | — |
| persistence | 0* | 0* | — | — | — | — | — | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.08* | 0.08* | — | — | — | — | — | — | — |
| open-meteo-gfs | 0.04* | 0.06* | — | — | — | — | — | — | — |
| persistence | 0.14* | 0.14* | — | — | — | — | — | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-ecmwf | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| open-meteo-gfs | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| persistence | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
