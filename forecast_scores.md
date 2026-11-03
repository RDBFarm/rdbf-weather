# RDBF forecast scorecard

_Actuals from station KMDPOOLE58 (122 days on file, through 2026-11-02) · lead 0 = same day, 7 = a week ahead._

### High temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 3.6 | 3.6 | 3.6 | 4.1 | 4.2 | 4.2 | 4.7 | 1.0* | — |
| open-meteo-ecmwf | 3.6 | 3.3 | 3.6 | 4.3 | 4.6 | 5.7 | 5.9 | 6.4 | 7.4 |
| open-meteo-gfs | 3.2 | 3.2 | 3.6 | 3.9 | 3.3 | 4.2 | 5.3 | 3.7 | 6.9 |
| persistence | 5.7 | 6.9 | 6.9 | 7.9 | 7.8 | 7.5 | 7.4 | 8.5 | 8.7 |

### High temperature — average error (°F, + = forecast ran warm)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | -3.5 | -3.3 | -3.3 | -3.6 | -2.9 | -2.3 | -1.7 | -1.0* | — |
| open-meteo-ecmwf | -3.5 | -3.1 | -3.5 | -3.6 | -3.5 | -3.3 | -2.3 | -2.8 | -5.5 |
| open-meteo-gfs | -3.1 | -2.9 | -3.3 | -3.8 | -3.2 | -3.8 | -3.8 | -1.8 | -4.4 |
| persistence | 1.7 | 2.3 | 3.1 | 3.6 | 2.9 | 2.9 | 2.8 | 2.9 | 4.4 |

### Low temperature — average miss (°F, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | 2.8 | 2.9 | 2.9 | 3.4 | 4.6 | 6.0 | 6.7 | — |
| open-meteo-ecmwf | 4.4 | 4.5 | 4.8 | 4.9 | 4.4 | 4.2 | 5.9 | 6.6 | 5.4 |
| open-meteo-gfs | 3.3 | 3.6 | 3.3 | 3.5 | 3.7 | 4.3 | 6.0 | 4.9 | 8.3 |
| persistence | 4.0 | 4.9 | 7.2 | 7.8 | 7.8 | 8.1 | 8.1 | 9.0 | 9.9 |

### Rain chance — Brier score (0 perfect, 0.25 = always saying 50%)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 0.072 | 0.049 | 0.044 | 0.021 | 0.008 | 0.029 | 0.036 | 0.000* | — |
| open-meteo-ecmwf | 0.020 | 0.021 | 0.024 | 0.014 | 0.005 | 0.008 | 0.019 | 0.035 | 0.042 |
| open-meteo-gfs | 0.095 | 0.062 | 0.034 | 0.025 | 0.002 | 0.008 | 0.014 | 0.020 | 0.022 |
| persistence | 0.133 | 0.211 | 0.278 | 0.235 | 0.188 | 0.200 | 0.214 | 0.231 | 0.333 |

### Rain — % of days the 50% call was right

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 87 | 95 | 94 | 94 | 100 | 93 | 93 | 100* | — |
| open-meteo-ecmwf | 100 | 95 | 94 | 100 | 100 | 100 | 100 | 100 | 98 |
| open-meteo-gfs | 79 | 89 | 94 | 94 | 100 | 100 | 100 | 100 | 100 |
| persistence | 87 | 79 | 72 | 76 | 81 | 80 | 79 | 77 | 67 |

### Rain amount — average miss (inches, lower is better)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | — | — | — | — | — | — | — | — | — |
| open-meteo-ecmwf | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.07 |
| open-meteo-gfs | 0.01 | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.07 | 0.00 | 0.08 |
| persistence | 0.02 | 0.03 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.04 |

### Days behind each number (high-temperature count)

| Source | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8-14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nws | 15 | 19 | 18 | 17 | 16 | 15 | 14 | 1 | 0 |
| open-meteo-ecmwf | 14 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 63 |
| open-meteo-gfs | 14 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 63 |
| persistence | 15 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 63 |

`*` = fewer than 10 days, treat as noise. `persistence` repeats the last known actual; a forecaster that cannot beat it is adding nothing. A rain day is 0.01 in or more at the station.
