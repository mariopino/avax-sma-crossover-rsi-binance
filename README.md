# Backtesting a mixed SMA crossover and RSI strategy on the AVAX-USDT pair

Backtesting a mixed SMA crossover and RSI strategy on the AVAX-USDT pair using [Backtesting.py](https://kernc.github.io/backtesting.py/) Python library.

This strategy beats Buy and Hold using last three months of data:

```
Return [%]                           86.08146
Buy & Hold Return [%]               -51.25941
```

The script does the following:

- Download 15min interval monthly OHLCV data from [Binance Data](https://data.binance.vision/?prefix=data/spot/monthly/klines/AVAXUSDT/)
- Initial run with predefined parameters
- Optimization
- Run with optimized parameters
- Generates a chart with indicators and trades (Chart.html)
- Generates a Heatmap for the different combination of slow and fast moving averages (Heatmap.html)
- Export trades to CSV file (Trades.csv)

The best results were achieved using a 5% stop loss for both SHORT and LONG trades.

# Installation

## Clone repository:

```
git clone https://github.com/mariopino/avax-sma-crossover-rsi-binance.git
cd avax-sma-crossover-rsi-binance
```

## Create virtual environment

### VSCode

To create local environments in VS Code using virtual environments or Anaconda, you can follow these steps: open the Command Palette (Ctrl+Shift+P), search for the Python: Create Environment command, and select it, then select Venv.

Select and activate an environment

Use the `Python: Select Interpreter` command from the Command Palette (Ctrl+Shift+P) and then select `.\.venv\Scripts\python.exe`.

### Linux

```
python -m venv myvenv
source myvenv/bin/activate
```

## Install dependencies

```
pip install backtesting
pip install pandas-ta
```

# Execute script

## Windows

```
python.exe SMACrossRSI.py
```

## Linux

```
python SMACrossRSI.py
```

# Results:

```
Initial Backtest Results (n1=40, n2=100, rsi_window=14, rsi_upper_bound=50, rsi_lower_bound=40):

Start                     2025-01-01 00:00:00
End                       2025-03-31 23:45:00
Duration                     89 days 23:45:00
Exposure Time [%]                    95.25463
Equity Final [$]                    18608.146
Equity Peak [$]                   19108.10816
Commissions [$]                    3889.71126
Return [%]                           86.08146
Buy & Hold Return [%]               -51.25941
Return (Ann.) [%]                  1141.06899
Volatility (Ann.) [%]              1202.04596
CAGR [%]                           1141.43086
Sharpe Ratio                          0.94927
Sortino Ratio                        26.08414
Calmar Ratio                         60.01055
Alpha [%]                            57.48241
Beta                                 -0.55793
Max. Drawdown [%]                   -19.01447
Avg. Drawdown [%]                    -2.98752
Max. Drawdown Duration       22 days 02:15:00
Avg. Drawdown Duration        1 days 06:31:00
# Trades                                   77
Win Rate [%]                         54.54545
Best Trade [%]                       20.88863
Worst Trade [%]                      -5.02882
Avg. Trade [%]                        1.21806
Max. Trade Duration           6 days 18:30:00
Avg. Trade Duration           1 days 02:43:00
Profit Factor                         2.46229
Expectancy [%]                         1.3303
SQN                                   2.30273
Kelly Criterion                       0.32072
_strategy                         SMACrossRSI

...

Optimized Backtest Results (n1=40, n2=100, rsi_upper_bound=50, rsi_lower_bound=40):

Start                     2025-01-01 00:00:00
End                       2025-03-31 23:45:00
Duration                     89 days 23:45:00
Exposure Time [%]                    95.25463
Equity Final [$]                    18608.146
Equity Peak [$]                   19108.10816
Commissions [$]                    3889.71126
Return [%]                           86.08146
Buy & Hold Return [%]               -51.25941
Return (Ann.) [%]                  1141.06899
Volatility (Ann.) [%]              1202.04596
CAGR [%]                           1141.43086
Sharpe Ratio                          0.94927
Sortino Ratio                        26.08414
Calmar Ratio                         60.01055
Alpha [%]                            57.48241
Beta                                 -0.55793
Max. Drawdown [%]                   -19.01447
Avg. Drawdown [%]                    -2.98752
Max. Drawdown Duration       22 days 02:15:00
Avg. Drawdown Duration        1 days 06:31:00
# Trades                                   77
Win Rate [%]                         54.54545
Best Trade [%]                       20.88863
Worst Trade [%]                      -5.02882
Avg. Trade [%]                        1.21806
Max. Trade Duration           6 days 18:30:00
Avg. Trade Duration           1 days 02:43:00
Profit Factor                         2.46229
Expectancy [%]                         1.3303
SQN                                   2.30273
Kelly Criterion                       0.32072
_strategy                 SMACrossRSI(n1=4...
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object

Best Run Trades:

     Type           EntryTime            ExitTime  EntryPrice  ExitPrice        PnL  ReturnPct        Duration
0   Short 2025-01-02 15:45:00 2025-01-03 08:30:00       39.35    40.0200  -169.5100  -1.702668 0 days 16:45:00
1    Long 2025-01-03 08:30:00 2025-01-04 09:00:00       40.02    41.5100   363.5600   3.723138 1 days 00:30:00
2   Short 2025-01-04 09:00:00 2025-01-04 22:00:00       41.51    42.8300  -320.7600  -3.179957 0 days 13:00:00
3    Long 2025-01-04 22:00:00 2025-01-05 01:45:00       42.83    42.0400  -179.3300  -1.844502 0 days 03:45:00
4   Short 2025-01-05 01:45:00 2025-01-05 23:30:00       42.04    43.0600  -230.5200  -2.426261 0 days 21:45:00
5    Long 2025-01-05 23:30:00 2025-01-06 23:15:00       43.06    43.7500   147.6600   1.602415 0 days 23:45:00
6   Short 2025-01-06 23:15:00 2025-01-10 07:00:00       43.75    37.3700  1358.9400  14.582857 3 days 07:45:00
7    Long 2025-01-10 07:00:00 2025-01-10 13:45:00       37.37    36.6100  -216.6000  -2.033717 0 days 06:45:00
8   Short 2025-01-10 13:45:00 2025-01-12 18:30:00       36.61    37.1600  -156.2000  -1.502322 2 days 04:45:00
9    Long 2025-01-12 18:30:00 2025-01-12 19:30:00       37.16    36.8600   -82.5000  -0.807320 0 days 01:00:00
10  Short 2025-01-12 19:30:00 2025-01-14 03:15:00       36.86    35.4200   394.5600   3.906674 1 days 07:45:00
11   Long 2025-01-14 03:15:00 2025-01-15 10:00:00       35.42    36.4300   297.9500   2.851496 1 days 06:45:00
12  Short 2025-01-15 10:00:00 2025-01-15 13:30:00       36.43    38.2620  -536.7760  -5.028822 0 days 03:30:00
13  Short 2025-01-16 08:45:00 2025-01-16 17:15:00       38.76    39.7100  -247.9500  -2.450980 0 days 08:30:00
14   Long 2025-01-16 17:15:00 2025-01-17 18:00:00       39.71    40.7000   244.5300   2.493075 1 days 00:45:00
15  Short 2025-01-17 18:00:00 2025-01-21 16:30:00       40.70    36.4600  1043.0400  10.417690 3 days 22:30:00
16   Long 2025-01-21 16:30:00 2025-01-22 14:15:00       36.46    36.7100    75.7500   0.685683 0 days 21:45:00
17  Short 2025-01-22 14:15:00 2025-01-22 17:45:00       36.71    37.2600  -165.5500  -1.498229 0 days 03:30:00
18   Long 2025-01-22 17:45:00 2025-01-23 00:45:00       37.26    36.6200  -186.2400  -1.717660 0 days 07:00:00
19  Short 2025-01-23 00:45:00 2025-01-24 08:15:00       36.62    35.8600   220.4000   2.075369 1 days 07:30:00
20   Long 2025-01-24 08:15:00 2025-01-24 20:30:00       35.86    35.9900    39.1300   0.362521 0 days 12:15:00
21  Short 2025-01-24 20:30:00 2025-01-25 18:30:00       35.99    36.6400  -195.0000  -1.806057 0 days 22:00:00
22   Long 2025-01-25 18:30:00 2025-01-26 21:15:00       36.64    37.3900   216.0000   2.046943 1 days 02:45:00
23  Short 2025-01-26 21:15:00 2025-01-28 04:15:00       37.39    34.1200   938.4900   8.745654 1 days 07:00:00
24   Long 2025-01-28 04:15:00 2025-01-28 09:30:00       34.12    33.8300   -98.8900  -0.849941 0 days 05:15:00
25  Short 2025-01-28 09:30:00 2025-01-30 01:30:00       33.83    33.2700   189.8400   1.655336 1 days 16:00:00
26   Long 2025-01-30 01:30:00 2025-01-31 00:15:00       33.27    34.1300   301.0000   2.584911 0 days 22:45:00
27  Short 2025-01-31 00:15:00 2025-01-31 15:45:00       34.13    35.8365  -593.8620  -5.000000 0 days 15:30:00
28  Short 2025-01-31 18:45:00 2025-02-03 19:00:00       34.66    27.4200  2345.7600  20.888632 3 days 00:15:00
29   Long 2025-02-03 19:00:00 2025-02-04 03:30:00       27.42    27.4800    29.6400   0.218818 0 days 08:30:00
30  Short 2025-02-04 03:30:00 2025-02-05 02:45:00       27.48    26.7800   344.4000   2.547307 0 days 23:15:00
31   Long 2025-02-05 02:45:00 2025-02-05 05:15:00       26.78    26.6500   -67.0800  -0.485437 0 days 02:30:00
32  Short 2025-02-05 05:15:00 2025-02-05 08:15:00       26.65    26.9200  -138.7800  -1.013133 0 days 03:00:00
33   Long 2025-02-05 08:15:00 2025-02-05 15:00:00       26.92    26.7000  -110.2200  -0.817236 0 days 06:45:00
34  Short 2025-02-05 15:00:00 2025-02-06 11:00:00       26.70    26.7100    -4.9900  -0.037453 0 days 20:00:00
35   Long 2025-02-06 11:00:00 2025-02-06 12:45:00       26.71    26.0800  -313.1100  -2.358667 0 days 01:45:00
36  Short 2025-02-06 12:45:00 2025-02-07 13:00:00       26.08    25.3600   356.4000   2.760736 1 days 00:15:00
37   Long 2025-02-07 13:00:00 2025-02-07 17:15:00       25.36    25.0100  -182.3500  -1.380126 0 days 04:15:00
38  Short 2025-02-07 17:15:00 2025-02-08 20:00:00       25.01    24.5800   223.1700   1.719312 1 days 02:45:00
39   Long 2025-02-08 20:00:00 2025-02-09 13:30:00       24.58    24.8100   123.0500   0.935720 0 days 17:30:00
40  Short 2025-02-09 13:30:00 2025-02-10 09:00:00       24.81    25.7300  -490.3600  -3.708182 0 days 19:30:00
41   Long 2025-02-10 09:00:00 2025-02-11 14:00:00       25.73    25.9100    88.7400   0.699572 1 days 05:00:00
42  Short 2025-02-11 14:00:00 2025-02-12 19:45:00       25.91    25.9500   -19.6400  -0.154381 1 days 05:45:00
43   Long 2025-02-12 19:45:00 2025-02-13 05:00:00       25.95    25.9900    19.4800   0.154143 0 days 09:15:00
44  Short 2025-02-13 05:00:00 2025-02-14 05:30:00       25.99    25.7500   116.4000   0.923432 1 days 00:30:00
45   Long 2025-02-14 05:30:00 2025-02-14 21:00:00       25.75    26.2200   231.2400   1.825243 0 days 15:30:00
46  Short 2025-02-14 21:00:00 2025-02-17 11:30:00       26.22    25.3700   416.5000   3.241800 2 days 14:30:00
47   Long 2025-02-17 11:30:00 2025-02-17 16:00:00       25.37    25.1400  -119.8300  -0.906583 0 days 04:30:00
48  Short 2025-02-17 16:00:00 2025-02-19 11:30:00       25.14    23.9800   602.0400   4.614161 1 days 19:30:00
49   Long 2025-02-19 11:30:00 2025-02-19 15:00:00       23.98    23.4900  -277.8300  -2.043369 0 days 03:30:00
50  Short 2025-02-19 15:00:00 2025-02-20 12:30:00       23.49    24.6540  -657.6600  -4.955300 0 days 21:30:00
51  Short 2025-02-21 15:45:00 2025-02-22 11:30:00       25.33    25.1700    79.3600   0.631662 0 days 19:45:00
52   Long 2025-02-22 11:30:00 2025-02-23 00:30:00       25.17    25.7000   265.0000   2.105681 0 days 13:00:00
53  Short 2025-02-23 00:30:00 2025-02-25 23:30:00       25.70    22.0400  1822.6800  14.241245 2 days 23:00:00
54   Long 2025-02-25 23:30:00 2025-02-26 12:30:00       22.04    21.9600   -52.8800  -0.362976 0 days 13:00:00
55  Short 2025-02-26 12:30:00 2025-02-27 06:00:00       21.96    22.5500  -388.8100  -2.686703 0 days 17:30:00
56   Long 2025-02-27 06:00:00 2025-02-27 15:00:00       22.55    22.7000    93.3000   0.665188 0 days 09:00:00
57  Short 2025-02-27 15:00:00 2025-02-28 19:45:00       22.70    22.2100   303.3100   2.158590 1 days 04:45:00
58   Long 2025-02-28 19:45:00 2025-03-01 06:30:00       22.21    22.0200  -122.3600  -0.855471 0 days 10:45:00
59  Short 2025-03-01 06:30:00 2025-03-02 03:45:00       22.02    21.9300    57.7800   0.408719 0 days 21:15:00
60   Long 2025-03-02 03:45:00 2025-03-02 14:15:00       21.93    21.8000   -83.7200  -0.592795 0 days 10:30:00
61  Short 2025-03-02 14:15:00 2025-03-02 15:30:00       21.80    22.8795  -693.0390  -4.951835 0 days 01:15:00
62  Short 2025-03-03 02:15:00 2025-03-08 19:15:00       24.16    20.6200  1939.9200  14.652318 5 days 17:00:00
63   Long 2025-03-08 19:15:00 2025-03-09 02:45:00       20.62    20.2900  -242.2200  -1.600388 0 days 07:30:00
64  Short 2025-03-09 02:45:00 2025-03-15 21:15:00       20.29    19.2100   789.4800   5.322819 6 days 18:30:00
65   Long 2025-03-15 21:15:00 2025-03-16 09:30:00       19.21    19.2000    -8.1000  -0.052056 0 days 12:15:00
66  Short 2025-03-16 09:30:00 2025-03-17 16:30:00       19.20    18.5500   524.5500   3.385417 1 days 07:00:00
67   Long 2025-03-17 16:30:00 2025-03-18 01:45:00       18.55    18.5900    34.4000   0.215633 0 days 09:15:00
68  Short 2025-03-18 01:45:00 2025-03-19 03:30:00       18.59    18.9900  -342.4000  -2.151694 1 days 01:45:00
69   Long 2025-03-19 03:30:00 2025-03-20 01:45:00       18.99    19.2900   245.1000   1.579779 0 days 22:15:00
70  Short 2025-03-20 01:45:00 2025-03-21 23:00:00       19.29    19.1500   113.9600   0.725765 1 days 21:15:00
71   Long 2025-03-21 23:00:00 2025-03-22 14:45:00       19.15    19.3200   139.7400   0.887728 0 days 15:45:00
72  Short 2025-03-22 14:45:00 2025-03-24 00:45:00       19.32    20.2755  -782.5545  -4.945652 1 days 10:00:00
73   Long 2025-03-24 01:15:00 2025-03-24 15:45:00       20.15    21.4800   988.1900   6.600496 0 days 14:30:00
74  Short 2025-03-24 15:45:00 2025-03-25 08:45:00       21.48    21.9400  -340.4000  -2.141527 0 days 17:00:00
75   Long 2025-03-25 08:45:00 2025-03-26 03:15:00       21.94    22.7100   543.6200   3.509572 0 days 18:30:00
76  Short 2025-03-26 03:15:00 2025-03-31 20:30:00       22.71    18.8200  2734.6700  17.129018 5 days 17:15:00
```