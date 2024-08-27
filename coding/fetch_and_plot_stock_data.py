import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_data(stock_symbol, start_date, end_date):
    """ Fetch stock data from Yahoo Finance. """
    return yf.download(stock_symbol, start=start_date, end=end_date)

def plot_stock_gains(stock_data_1, stock_data_2, label1, label2):
    """ Plot the stock gains from the beginning of the year to the current date. """
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data_1['Close'] / stock_data_1['Close'].iloc[0] - 1, label=label1)
    plt.plot(stock_data_2['Close'] / stock_data_2['Close'].iloc[0] - 1, label=label2)
    plt.title('Stock Gains YTD for NVDA and TSLA')
    plt.xlabel('Date')
    plt.ylabel('Gain')
    plt.legend()
    plt.savefig('ytd_stock_gains.png')
    plt.show()

# Initial parameters
symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-08-27'

# Fetch data
nvda_data = fetch_data(symbols[0], start_date, end_date)
tsla_data = fetch_data(symbols[1], start_date, end_date)

# Plot data
plot_stock_gains(nvda_data, tsla_data, symbols[0], symbols[1])