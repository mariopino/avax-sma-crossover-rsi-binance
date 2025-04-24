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
year = 2024 # From 2020 to 2025
months = range(1, 13) # Months to load e.g. range(1, 13) for all months or [1, 3] for Jan and Mar
interval = '1h' # Data interval (e.g. '1m', '5m', '15m', '30m', '1h', '4h', '1d')
timestamp_unit = 'ms' # For 2025 data, use 'us' for microseconds
cash = 10000  # Initial cash amount in USD
commission = 0.002  # Commission per trade
exclusive_orders = True  # Only one order at a time
n1 = 12  # Fast SMA
n2 = 118  # Slow SMA
rsi_window = 14  # RSI window
rsi_upper_bound = 50 # Upper bound for RSI
rsi_lower_bound = 40 # Lower bound for RSI
do_optimization = False  # Set to True to run optimization
maximize = 'Return [%]' # 'Return [%]', 'Sharpe Ratio', 'Max. Drawdown [%]', 'Win Rate [%]', 'Profit Factor', 'Expectancy [%]'


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

        # Compute RSI using TA
        close = pd.Series(self.data.Close, index=self.data.index)
        rsi = ta.rsi(close, window=rsi_window)
        self.rsi = self.I(lambda: rsi)

    def next(self):
        if crossover(self.sma1, self.sma2) and self.rsi[-1] > rsi_upper_bound:
            # Check if we are not already in a position
            if not self.position.is_long:
                # Close any existing short position
                if self.position.is_short:
                    self.position.close()
                # Enter long position
                self.buy(sl=self.data.Close[-1] * 0.95)
                # self.buy()

        elif crossover(self.sma2, self.sma1) or self.rsi[-1] < rsi_lower_bound:
            # Check if we are not already in a position
            if not self.position.is_short:
                # Close any existing long position
                if self.position.is_long:
                    self.position.close()
                # Enter short position
                self.sell(sl=self.data.Close[-1] * 1.05)
                # self.sell()

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
        n1=range(2, 52, 2),  # Fast SMA from 2 to 50, step 2
        n2=range(50, 202, 2),  # Slow SMA from 50 to 200, step 2
        #rsi_window=range(5, 31, 2),  # RSI window from 5 to 30, step 2
        #rsi_upper_bound=range(50, 62, 2),  # RSI upper bound from 50 to 60, step 2
        #rsi_lower_bound=range(40, 52, 2),  # RSI lower bound from 40 to 50, step 2
        maximize=maximize,  # Maximize param
        constraint=lambda p: p.n1 < p.n2, # and p.rsi_upper_bound > p.rsi_lower_bound
        return_heatmap=True # Return heatmap data
    )

    # Print optimization results
    best_n1 = optimization_results._strategy.n1
    best_n2 = optimization_results._strategy.n2
    # best_rsi_upper_bound = optimization_results._strategy.rsi_upper_bound
    # best_rsi_lower_bound = optimization_results._strategy.rsi_lower_bound
    best_rsi_upper_bound = rsi_upper_bound
    best_rsi_lower_bound = rsi_lower_bound
    print(f"\nOptimized Backtest Results (n1={best_n1}, n2={best_n2}, rsi_upper_bound={rsi_upper_bound}, rsi_lower_bound={rsi_lower_bound}):\n")
    print(optimization_results)

    # Run the backtest with the best parameters
    best_run = bt.run(n1=best_n1, n2=best_n2, rsi_upper_bound=best_rsi_upper_bound, rsi_lower_bound=best_rsi_lower_bound)

    # Plot the results of the best run
    bt.plot(filename='Chart.html')

    # Plot Heatmap
    plot_heatmaps(heatmap, agg='mean', filename='Heatmap.html')

    # Print the best run trades
    print_and_export_trades(best_run['_trades'])

