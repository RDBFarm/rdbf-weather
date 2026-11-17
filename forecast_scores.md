# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (136 days on file, through 2026-11-16) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.8 | 2.7 | 3.3 | 3.9 | 3.9 | 4.6 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.3 | 3.9 | 4.0 | 5.2 | 5.1 | 5.5 | 8.2 |
| open-meteo-gfs | 2.7 | 3.6 | 3.3 | 3.5 | 2.9 | 4.3 | 5.9 | 5.6 | 8.4 |
| persistence | 5.7 | 7.7 | 8.7 | 9.1 | 8.3 | 7.7 | 6.9 | 8.7 | 9.6 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.5 | -2.6 | -2.9 | -2.6 | -2.6 | -2.3 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.8 | -3.0 | -3.4 | -3.1 | -3.2 | -3.2 | -3.2 | -5.0 |
| open-meteo-gfs | -2.6 | -3.5 | -3.0 | -3.5 | -2.7 | -4.1 | -4.7 | -4.5 | -6.4 |
| persistence | 1.8 | 1.9 | 2.8 | 3.8 | 3.9 | 3.9 | 3.9 | 4.4 | 4.9 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 3.1 | 3.1 | 3.1 | 3.6 | 4.5 | 5.6 | 6.3 | — |
| open-meteo-ecmwf | 4.2 | 4.5 | 4.9 | 4.9 | 4.9 | 4.7 | 5.5 | 6.3 | 6.7 |
| open-meteo-gfs | 3.1 | 3.8 | 3.5 | 4.1 | 4.3 | 4.9 | 6.0 | 5.7 | 8.1 |
| persistence | 4.3 | 6.9 | 8.7 | 9.2 | 8.3 | 8.1 | 8.1 | 8.8 | 9.3 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.057 | 0.069 | 0.048 | 0.025 | 0.042 | 0.059 | 0.079 | 0.000* | — |
| open-meteo-ecmwf | 0.016 | 0.049 | 0.051 | 0.029 | 0.032 | 0.050 | 0.065 | 0.089 | 0.147 |
| open-meteo-gfs | 0.074 | 0.073 | 0.057 | 0.031 | 0.037 | 0.048 | 0.064 | 0.077 | 0.109 |
| persistence | 0.158 | 0.303 | 0.344 | 0.323 | 0.267 | 0.207 | 0.214 | 0.296 | 0.292 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 91 | 94 | 97 | 97 | 90 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 91 | 94 | 97 | 93 | 90 | 86 | 93 | 84 |
| open-meteo-gfs | 83 | 88 | 91 | 94 | 93 | 86 | 93 | 89 | 87 |
| persistence | 84 | 70 | 66 | 68 | 73 | 79 | 79 | 70 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.03 | 0.02 | 0.01 | 0.10 | 0.03 | 0.10 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.05 | 0.11 | 0.15 | 0.11 |
| persistence | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 19 | 33 | 32 | 31 | 30 | 29 | 28 | 1 | 0 |
| open-meteo-ecmwf | 18 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 150 |
| open-meteo-gfs | 18 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 161 |
| persistence | 19 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 161 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
