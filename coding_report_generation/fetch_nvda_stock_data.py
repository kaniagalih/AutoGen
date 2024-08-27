# filename: fetch_nvda_stock_data.py
import yfinance as yf
import pandas as pd

# Define the ticker symbol and the time period
ticker_symbol = "NVDA"
start_date = "2024-07-27"
end_date = "2024-08-27"

# Fetch historical data from Yahoo Finance
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the data to a CSV file for further analysis
data.to_csv('nvda_stock_data.csv')

# Print some basic statistics and data to give an overview
print("Data for NVDA from 2024-07-27 to 2024-08-27:")
print(data.head())  # Prints the first 5 rows of the dataframe
print("\nSummary Statistics:")
print(data.describe())  # Provides descriptive statistics