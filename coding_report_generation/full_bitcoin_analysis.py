# filename: full_bitcoin_analysis.py

import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_bitcoin_prices(start_date, end_date):
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range'
    params = {
        'vs_currency': 'usd',
        'from': pd.Timestamp(start_date).timestamp(),
        'to': pd.Timestamp(end_date).timestamp()
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    else:
        print("Failed to fetch data:", response.status_code)
        return pd.DataFrame()

def analyze_and_plot(bitcoin_prices):
    print('Highest Price:', bitcoin_prices['price'].max())
    print('Lowest Price:', bitcoin_prices['price'].min())
    print('Average Price:', bitcoin_prices['price'].mean())
    plt.figure(figsize=(14, 7))
    plt.plot(bitcoin_prices, label='Bitcoin Price', color='orange')
    plt.title('Bitcoin Price Trend from 2024-07-27 to 2024-08-27')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.show()

# Dates for the past month
start_date = '2024-07-27'
end_date = '2024-08-27'

# Fetching and analyzing the Bitcoin price data
bitcoin_prices = fetch_bitcoin_prices(start_date, end_date)
analyze_and_plot(bitcoin_prices)