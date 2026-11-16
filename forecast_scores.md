# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (135 days on file, through 2026-11-15) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.0 | 2.8 | 2.8 | 3.3 | 3.8 | 3.9 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.1 | 2.9 | 3.3 | 3.8 | 4.0 | 5.2 | 5.0 | 5.3 | 8.3 |
| open-meteo-gfs | 2.7 | 3.6 | 3.3 | 3.6 | 2.9 | 4.3 | 5.8 | 5.6 | 8.5 |
| persistence | 5.7 | 7.7 | 8.7 | 9.2 | 8.2 | 7.4 | 7.0 | 8.8 | 9.5 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -2.9 | -2.5 | -2.6 | -2.8 | -2.5 | -2.5 | -2.3 | -1.0* | — |
| open-meteo-ecmwf | -3.0 | -2.8 | -3.0 | -3.4 | -3.1 | -3.1 | -3.1 | -3.0 | -5.4 |
| open-meteo-gfs | -2.6 | -3.4 | -3.0 | -3.5 | -2.7 | -4.0 | -4.6 | -4.5 | -6.4 |
| persistence | 1.8 | 2.2 | 3.1 | 3.8 | 3.7 | 3.5 | 3.9 | 4.3 | 4.6 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.9 | 3.1 | 3.1 | 3.6 | 4.5 | 5.7 | 6.5 | — |
| open-meteo-ecmwf | 4.2 | 4.3 | 4.7 | 4.9 | 4.8 | 4.6 | 5.6 | 6.4 | 6.3 |
| open-meteo-gfs | 3.1 | 3.8 | 3.5 | 4.1 | 4.3 | 5.0 | 6.1 | 5.6 | 8.2 |
| persistence | 4.3 | 6.8 | 8.6 | 9.0 | 8.3 | 8.2 | 8.2 | 8.6 | 8.9 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.057 | 0.071 | 0.049 | 0.026 | 0.043 | 0.061 | 0.082 | 0.000* | — |
| open-meteo-ecmwf | 0.016 | 0.051 | 0.052 | 0.030 | 0.033 | 0.052 | 0.067 | 0.092 | 0.147 |
| open-meteo-gfs | 0.074 | 0.075 | 0.059 | 0.032 | 0.038 | 0.050 | 0.066 | 0.080 | 0.113 |
| persistence | 0.158 | 0.312 | 0.355 | 0.300 | 0.276 | 0.214 | 0.222 | 0.308 | 0.292 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 89 | 91 | 94 | 97 | 97 | 89 | 89 | 100* | — |
| open-meteo-ecmwf | 100 | 91 | 94 | 97 | 93 | 89 | 85 | 92 | 84 |
| open-meteo-gfs | 83 | 88 | 90 | 93 | 93 | 86 | 93 | 88 | 86 |
| persistence | 84 | 69 | 65 | 70 | 72 | 79 | 78 | 69 | 71 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.01 | 0.02 | 0.02 | 0.04 | 0.02 | 0.01 | 0.10 | 0.03 | 0.09 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.05 | 0.11 | 0.15 | 0.11 |
| persistence | 0.02 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 19 | 32 | 31 | 30 | 29 | 28 | 27 | 1 | 0 |
| open-meteo-ecmwf | 18 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 143 |
| open-meteo-gfs | 18 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 154 |
| persistence | 19 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 154 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
