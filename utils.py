import numpy as np
import pandas as pd
import csv

#
# Load data frame from CSV files
#

def load_data(ticker_name, year, months, interval, timestamp_unit):
    """
    Load data from CSV files for the specified ticker, year, months, interval and timestamp unit.
    """
    csv_filenames = []
    for month in months:
        # Generate the filename for each month
        filename = f"data/spot/monthly/klines/{ticker_name}/{interval}/{ticker_name}-{interval}-{year}-{month:02d}.csv"
        csv_filenames.append(filename)

    # Prepare the data frame
    df = pd.DataFrame(read_csvs(csv_filenames))
    df.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore']
    df['Time'] = pd.to_datetime(df['Time'].astype('int64'), unit=timestamp_unit)
    df.index = pd.DatetimeIndex(df['Time'])
    df_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df[df_columns]
    df[df_columns] = df[df_columns].astype(float)

    return df


#
# Function to read multiple CSV files
#

def read_csvs(filenames):
    """
    This function will iterate over the lines of multiple csv files as if
    you were iterating over one long one
    """
    for fn in filenames:
        with open(fn, 'r') as fp:
            csv_file = csv.reader(fp)
            yield from csv_file


#
# Function to print and export trades
#

def print_and_export_trades(trades):

    # Add the trade type
    trades['Type'] = np.where(trades['Size'] > 0, 'Long', 'Short')

    # Compute return in percentage
    trades['ReturnPct'] = np.where(
        trades['Type'] == 'Long',
        (trades['ExitPrice'] - trades['EntryPrice']) / trades['EntryPrice'] * 100,
        (trades['EntryPrice'] - trades['ExitPrice']) / trades['EntryPrice'] * 100
    )

    # Cleanup and reorder columns
    useful_cols = ['Type', 'EntryTime', 'ExitTime', 'EntryPrice', 'ExitPrice', 'PnL', 'ReturnPct', 'Duration']
    trades = trades[useful_cols]

    # Print the trades
    print("\nTrades:\n")
    print(trades.to_string())

    # Save trades to a CSV file
    trades.to_csv('Trades.csv', index=False)
