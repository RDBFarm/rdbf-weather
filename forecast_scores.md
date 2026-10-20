# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (108 days on file, through 2026-10-19) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 5.8* | 5.8* | 6.0* | 8.3* | 7.0* | 7.0* | — | — | — |
| open-meteo-ecmwf | 2.2* | 2.5* | 2.3* | 4.8* | 6.4* | 6.7* | — | — | — |
| open-meteo-gfs | 2.4* | 3.5* | 4.7* | 7.2* | 4.1* | 3.7* | — | — | — |
| persistence | 10.5* | 10.8* | 13.0* | 17.3* | 20.0* | 14.0* | — | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -5.2* | -5.8* | -6.0* | -8.3* | -7.0* | -7.0* | — | — | — |
| open-meteo-ecmwf | -1.8* | -1.9* | -2.3* | -4.8* | -6.4* | -6.7* | — | — | — |
| open-meteo-gfs | -2.2* | -3.2* | -3.3* | -7.2* | -4.1* | -3.7* | — | — | — |
| persistence | 6.5* | 8.0* | 13.0* | 17.3* | 20.0* | 14.0* | — | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8* | 4.0* | 4.0* | 1.5* | 1.0* | — | — | — |
| open-meteo-ecmwf | 3.4* | 3.7* | 4.6* | 6.1* | 4.6* | 5.0* | — | — | — |
| open-meteo-gfs | 2.2* | 1.8* | 2.3* | 1.9* | 1.8* | 3.4* | — | — | — |
| persistence | 6.8* | 10.4* | 18.8* | 19.0* | 19.0* | 15.0* | — | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.269* | 0.185* | 0.197* | 0.117* | 0.009* | 0.002* | — | — | — |
| open-meteo-ecmwf | 0.070* | 0.079* | 0.108* | 0.081* | 0.034* | 0.062* | — | — | — |
| open-meteo-gfs | 0.332* | 0.235* | 0.153* | 0.141* | 0.005* | 0.001* | — | — | — |
| persistence | 0.500* | 0.800* | 1.000* | 0.667* | 0.000* | 0.000* | — | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 50* | 80* | 75* | 67* | 100* | 100* | — | — | — |
| open-meteo-ecmwf | 100* | 80* | 75* | 100* | 100* | 100* | — | — | — |
| open-meteo-gfs | 25* | 60* | 75* | 67* | 100* | 100* | — | — | — |
| persistence | 50* | 20* | 0* | 33* | 100* | 100* | — | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.06* | 0.04* | 0.01* | 0.01* | 0.00* | 0.00* | — | — | — |
| open-meteo-gfs | 0.05* | 0.04* | 0.03* | 0.02* | 0.00* | 0.00* | — | — | — |
| persistence | 0.09* | 0.12* | 0.12* | 0.05* | 0.00* | 0.00* | — | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4 | 5 | 4 | 3 | 2 | 1 | 0 | 0 | 0 |
| open-meteo-ecmwf | 4 | 5 | 4 | 3 | 2 | 1 | 0 | 0 | 0 |
| open-meteo-gfs | 4 | 5 | 4 | 3 | 2 | 1 | 0 | 0 | 0 |
| persistence | 4 | 5 | 4 | 3 | 2 | 1 | 0 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
