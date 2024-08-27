# filename: fetch_bitcoin_data.py

import requests
import pandas as pd

def fetch_bitcoin_prices(start_date, end_date):
    # URL for the CoinGecko API endpoint
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range'
    
    # Parameters for the API request
    params = {
        'vs_currency': 'usd',
        'from': pd.Timestamp(start_date).timestamp(),
        'to': pd.Timestamp(end_date).timestamp()
    }
    
    # Making the request
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the prices data and convert it into a DataFrame
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    else:
        print("Failed to fetch data:", response.status_code)
        return pd.DataFrame()

# Dates for the past month
start_date = '2024-07-27'
end_date = '2024-08-27'

# Fetching the Bitcoin price data
bitcoin_prices = fetch_bitcoin_prices(start_date, end_date)
print(bitcoin_prices.head())  # Display the first few rows of the data
print(bitcoin_prices.tail())  # Display the last few rows of the data
