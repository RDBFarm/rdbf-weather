# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (115 days on file, through 2026-10-26) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.9 | 4.2 | 4.3 | 5.0 | 4.6* | 4.0* | 3.7* | 1.0* | — |
| open-meteo-ecmwf | 3.2* | 3.5 | 3.6 | 4.6 | 5.0* | 5.4* | 5.8* | 5.3* | 6.6 |
| open-meteo-gfs | 2.6* | 3.2 | 3.9 | 4.3 | 3.2* | 3.9* | 4.2* | 2.9* | 5.2 |
| persistence | 5.6 | 6.9 | 7.6 | 8.7 | 8.6* | 7.4* | 9.6* | 12.8* | 14.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.7 | -4.2 | -4.3 | -5.0 | -4.6* | -4.0* | -3.1* | -1.0* | — |
| open-meteo-ecmwf | -3.0* | -3.2 | -3.6 | -4.6 | -5.0* | -5.4* | -5.8* | -5.0* | -6.6 |
| open-meteo-gfs | -2.5* | -3.1 | -3.4 | -4.3 | -3.2* | -3.9* | -4.2* | -1.6* | -3.4 |
| persistence | 2.8 | 2.8 | 3.8 | 5.9 | 5.9* | 6.1* | 6.7* | 8.2* | 13.2 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.7 | 3.2 | 3.0 | 3.1* | 4.0* | 5.7* | 7.3* | — |
| open-meteo-ecmwf | 4.0* | 4.3 | 4.8 | 4.9 | 4.1* | 3.9* | 4.9* | 5.7* | 7.8 |
| open-meteo-gfs | 3.1* | 3.4 | 3.3 | 3.3 | 3.4* | 3.5* | 4.8* | 5.0* | 7.8 |
| persistence | 3.9 | 5.2 | 7.9 | 8.9 | 9.6* | 10.5* | 11.0* | 13.0* | 18.0 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.108 | 0.077 | 0.072 | 0.035 | 0.004* | 0.002* | 0.003* | 0.000* | — |
| open-meteo-ecmwf | 0.031* | 0.033 | 0.039 | 0.024 | 0.008* | 0.012* | 0.010* | 0.018* | 0.085 |
| open-meteo-gfs | 0.147* | 0.098 | 0.055 | 0.042 | 0.003* | 0.002* | 0.002* | 0.002* | 0.015 |
| persistence | 0.200 | 0.333 | 0.455 | 0.400 | 0.333* | 0.375* | 0.429* | 0.500* | 0.400 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 80 | 92 | 91 | 90 | 100* | 100* | 100* | 100* | — |
| open-meteo-ecmwf | 100* | 92 | 91 | 100 | 100* | 100* | 100* | 100* | 93 |
| open-meteo-gfs | 67* | 83 | 91 | 90 | 100* | 100* | 100* | 100* | 100 |
| persistence | 80 | 67 | 55 | 60 | 67* | 62* | 57* | 50* | 60 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02* | 0.02 | 0.00 | 0.00 | 0.00* | 0.00* | 0.00* | 0.00* | 0.02 |
| open-meteo-gfs | 0.02* | 0.02 | 0.01 | 0.01 | 0.00* | 0.00* | 0.00* | 0.00* | 0.00 |
| persistence | 0.03 | 0.05 | 0.05 | 0.03 | 0.04* | 0.04* | 0.05* | 0.05* | 0.05 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 10 | 12 | 11 | 10 | 9 | 8 | 7 | 1 | 0 |
| open-meteo-ecmwf | 9 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 15 |
| open-meteo-gfs | 9 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 15 |
| persistence | 10 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 15 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
