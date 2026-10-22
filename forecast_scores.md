# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (110 days on file, through 2026-10-21) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 4.8* | 5.0* | 5.2* | 6.6* | 5.8* | 5.3* | 4.5* | 1.0* | — |
| open-meteo-ecmwf | 2.6* | 2.9* | 3.1* | 4.6* | 4.9* | 5.5* | 3.1* | 5.4* | — |
| open-meteo-gfs | 2.4* | 3.6* | 4.5* | 5.5* | 3.8* | 3.9* | 1.8* | 1.4* | — |
| persistence | 8.0* | 9.1* | 10.8* | 13.4* | 14.2* | 13.0* | 17.0* | 16.0* | — |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -4.5* | -5.0* | -5.2* | -6.6* | -5.8* | -5.3* | -4.5* | -1.0* | — |
| open-meteo-ecmwf | -2.3* | -2.4* | -3.1* | -4.6* | -4.9* | -5.5* | -3.1* | -5.4* | — |
| open-meteo-gfs | -2.2* | -3.4* | -3.5* | -5.5* | -3.8* | -3.9* | -1.8* | 1.4* | — |
| persistence | 4.7* | 4.9* | 6.5* | 11.4* | 14.2* | 13.0* | 17.0* | 16.0* | — |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.3* | 4.0* | 4.0* | 3.2* | 4.0* | 5.0* | 5.0* | — |
| open-meteo-ecmwf | 4.3* | 4.4* | 5.2* | 6.2* | 5.8* | 6.2* | 4.8* | 7.7* | — |
| open-meteo-gfs | 3.4* | 2.6* | 2.9* | 2.6* | 2.7* | 4.1* | 9.1* | 8.8* | — |
| persistence | 5.0* | 8.1* | 12.8* | 15.6* | 19.5* | 18.3* | 16.5* | 12.0* | — |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.179* | 0.132* | 0.132* | 0.071* | 0.008* | 0.004* | 0.001* | 0.000* | — |
| open-meteo-ecmwf | 0.047* | 0.057* | 0.072* | 0.048* | 0.018* | 0.028* | 0.025* | 0.006* | — |
| open-meteo-gfs | 0.221* | 0.168* | 0.102* | 0.085* | 0.006* | 0.005* | 0.001* | 0.001* | — |
| persistence | 0.333* | 0.571* | 0.833* | 0.800* | 0.500* | 0.333* | 0.000* | 0.000* | — |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 67* | 86* | 83* | 80* | 100* | 100* | 100* | 100* | — |
| open-meteo-ecmwf | 100* | 86* | 83* | 100* | 100* | 100* | 100* | 100* | — |
| open-meteo-gfs | 50* | 71* | 83* | 80* | 100* | 100* | 100* | 100* | — |
| persistence | 67* | 43* | 17* | 20* | 50* | 67* | 100* | 100* | — |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.04* | 0.03* | 0.01* | 0.01* | 0.00* | 0.00* | 0.00* | 0.00* | — |
| open-meteo-gfs | 0.03* | 0.03* | 0.02* | 0.01* | 0.00* | 0.00* | 0.00* | 0.00* | — |
| persistence | 0.06* | 0.09* | 0.08* | 0.07* | 0.08* | 0.05* | 0.00* | 0.00* | — |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 6 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| open-meteo-ecmwf | 6 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| open-meteo-gfs | 6 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| persistence | 6 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
