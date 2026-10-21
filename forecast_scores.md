# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (109 days on file, through 2026-10-20) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 5.0* | 5.5* | 5.6* | 7.2* | 6.7* | 7.0* | 6.0* | — | — |
| open-meteo-ecmwf | 2.6* | 2.8* | 2.6* | 4.8* | 4.8* | 6.5* | 4.6* | — | — |
| open-meteo-gfs | 2.6* | 3.7* | 4.5* | 6.1* | 4.4* | 3.7* | 2.8* | — | — |
| persistence | 8.8* | 10.3* | 12.2* | 15.5* | 14.3* | 16.0* | 12.0* | — | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -4.6* | -5.5* | -5.6* | -7.2* | -6.7* | -7.0* | -6.0* | — | — |
| open-meteo-ecmwf | -2.4* | -2.3* | -2.6* | -4.8* | -4.8* | -6.5* | -4.6* | — | — |
| open-meteo-gfs | -2.4* | -3.5* | -3.3* | -6.1* | -4.4* | -3.7* | -2.8* | — | — |
| persistence | 4.8* | 5.3* | 8.6* | 15.5* | 14.3* | 16.0* | 12.0* | — | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.0* | 4.2* | 4.0* | 2.3* | 2.5* | 4.0* | — | — |
| open-meteo-ecmwf | 4.0* | 4.2* | 5.2* | 6.6* | 5.8* | 3.8* | 1.8* | — | — |
| open-meteo-gfs | 2.9* | 2.3* | 2.8* | 2.6* | 2.4* | 4.7* | 8.4* | — | — |
| persistence | 6.0* | 9.0* | 15.0* | 19.5* | 19.0* | 18.0* | 12.0* | — | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.215* | 0.154* | 0.158* | 0.088* | 0.009* | 0.005* | 0.000* | — | — |
| open-meteo-ecmwf | 0.056* | 0.066* | 0.087* | 0.061* | 0.024* | 0.036* | 0.040* | — | — |
| open-meteo-gfs | 0.265* | 0.196* | 0.122* | 0.106* | 0.006* | 0.005* | 0.000* | — | — |
| persistence | 0.400* | 0.667* | 1.000* | 0.750* | 0.333* | 0.000* | 0.000* | — | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 60* | 83* | 80* | 75* | 100* | 100* | 100* | — | — |
| open-meteo-ecmwf | 100* | 83* | 80* | 100* | 100* | 100* | 100* | — | — |
| open-meteo-gfs | 40* | 67* | 80* | 75* | 100* | 100* | 100* | — | — |
| persistence | 60* | 33* | 0* | 25* | 67* | 100* | 100* | — | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.04* | 0.03* | 0.01* | 0.01* | 0.00* | 0.00* | 0.00* | — | — |
| open-meteo-gfs | 0.04* | 0.04* | 0.02* | 0.02* | 0.00* | 0.00* | 0.00* | — | — |
| persistence | 0.07* | 0.10* | 0.10* | 0.08* | 0.05* | 0.00* | 0.00* | — | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 5 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 0 |
| open-meteo-ecmwf | 5 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 0 |
| open-meteo-gfs | 5 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 0 |
| persistence | 5 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
