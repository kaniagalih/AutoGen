import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_stock_prices(stock_symbols, start_date, end_date):
    # This is a mock function for demonstration.
    # Generate a date range from start_date to end_date
    dates = pd.date_range(start=start_date, end=end_date, freq='B')
    
    # Generate mock stock prices
    data = {}
    for symbol in stock_symbols:
        # Let's pretend the stock price starts at 100 and increments slightly every day
        data[symbol] = range(100, 100 + len(dates))
    
    # Create a DataFrame
    stock_prices = pd.DataFrame(data, index=dates)
    return stock_prices

def plot_stock_prices(stock_prices, filename):
    stock_prices.plot(title='Stock Prices YTD')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(filename)
    plt.close()

def main():
    stock_symbols = ['NVDA', 'TSLA']
    start_date = '2024-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')  # Use today's date
    
    # Get mock stock prices
    stock_prices = get_stock_prices(stock_symbols, start_date, end_date)
    
    # Plot and save the stock prices
    plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')
    print("Stock prices plotted and saved to 'stock_prices_YTD_plot.png'.")

if __name__ == "__main__":
    main()