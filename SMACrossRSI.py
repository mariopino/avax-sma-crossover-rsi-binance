from backtesting import Backtest, Strategy
from backtesting.lib import crossover, plot_heatmaps
from backtesting.test import SMA
import pandas as pd
import pandas_ta as ta

from utils import load_data, print_and_export_trades

#
# Backtest parameters
#

ticker_name = 'AVAXUSDT'
year = 2025 # From 2020 to 2025
months = range(1, 4) # Months to load e.g. range(1, 13) for all months or [1, 3] for Jan and Mar
interval = '1h' # Data interval (e.g. '1m', '5m', '15m', '30m', '1h', '4h', '1d')
timestamp_unit = 'us' # For 2025 data, use 'us' for microseconds

cash = 10000  # Initial cash amount in USD
commission = 0.002  # Commission per trade
exclusive_orders = True  # Only one order at a time
n1 = 5  # Fast SMA
n2 = 90  # Slow SMA
rsi_window = 10  # RSI window
rsi_upper_bound = 54 # Upper bound for RSI
rsi_lower_bound = 44 # Lower bound for RSI
do_optimization = True  # Set to True to run optimization
maximize = 'Return [%]' # 'Return [%]', 'Sharpe Ratio', 'Max. Drawdown [%]', 'Win Rate [%]', 'Profit Factor', 'Expectancy [%]'
stop_loss = 0.05  # Stop loss percentage (5%)

#
# Load data
#

df = load_data(ticker_name, year, months, interval, timestamp_unit)
# print("Data:\n")
# print(binance_data.head())
# print("\n...\n")
# print(binance_data.tail())

#
# Define the strategy
#

class SMACrossRSI(Strategy):
    n1 = n1
    n2 = n2
    rsi_window = rsi_window
    rsi_upper_bound = rsi_upper_bound
    rsi_lower_bound = rsi_lower_bound

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

        # When optimizing RSI window sizes, short windows might lead to NaN values at the beginning of the series.
        # To prevent issues with self.rsi[-1], pad/fill missing RSI values.
        rsi = ta.rsi(pd.Series(close, index=self.data.index), length=self.rsi_window).fillna(50)
        self.rsi = self.I(lambda: rsi)

    def next(self):
        if crossover(self.sma1, self.sma2) and self.rsi[-1] > self.rsi_upper_bound:
            # Check if we are not already in a position
            if not self.position.is_long:
                # Close any existing short position
                if self.position.is_short:
                    self.position.close()
                # Enter long position
                self.buy(sl=self.data.Close[-1] * (1 - stop_loss))

        elif crossover(self.sma2, self.sma1) or self.rsi[-1] < self.rsi_lower_bound:
            # Check if we are not already in a position
            if not self.position.is_short:
                # Close any existing long position
                if self.position.is_long:
                    self.position.close()
                # Enter short position
                self.sell(sl=self.data.Close[-1] * (1 + stop_loss))

#
# Initialize the backtest
#

bt = Backtest(df, SMACrossRSI, cash=cash, commission=commission, exclusive_orders=exclusive_orders)

#
# Print results of the backtest
#

print(f"\nInitial Backtest Results (n1={n1}, n2={n2}, rsi_window={rsi_window}, rsi_upper_bound={rsi_upper_bound}, rsi_lower_bound={rsi_lower_bound}):\n")
results = bt.run()
print(results)

#
# Optimization
#

if not do_optimization:

    bt.plot(filename='Chart.html')
    print_and_export_trades(results['_trades'])
    exit()

else:

    # Run optimization
    optimization_results, heatmap = bt.optimize(
        n1=range(5, 30, 5),
        n2=range(40, 100, 10),
        rsi_window=range(10, 21, 5),
        rsi_upper_bound=range(52, 58, 2),
        rsi_lower_bound=range(42, 48, 2),
        maximize=maximize,  # Maximize param
        constraint=lambda p: p.n1 < p.n2  and p.rsi_upper_bound > p.rsi_lower_bound,
        return_heatmap=True # Return heatmap data
    )

    # Print optimization results
    best_n1 = optimization_results._strategy.n1
    best_n2 = optimization_results._strategy.n2
    best_rsi_upper_bound = optimization_results._strategy.rsi_upper_bound
    best_rsi_lower_bound = optimization_results._strategy.rsi_lower_bound
    best_rsi_window = optimization_results._strategy.rsi_window

    print(f"\nOptimized Backtest Results (n1={best_n1}, n2={best_n2}, rsi_upper_bound={best_rsi_upper_bound}, rsi_lower_bound={best_rsi_lower_bound}, rsi_window={best_rsi_window}):\n")
    print(optimization_results)

    # Run the backtest with the best parameters
    best_run = bt.run(n1=best_n1, n2=best_n2, rsi_upper_bound=best_rsi_upper_bound, rsi_lower_bound=best_rsi_lower_bound, rsi_window=best_rsi_window)

    # Plot the results of the best run
    bt.plot(filename='Chart.html')

    # Plot Heatmap
    plot_heatmaps(heatmap, agg='mean', filename='Heatmap.html')

    # Print the best run trades
    print_and_export_trades(best_run['_trades'])

