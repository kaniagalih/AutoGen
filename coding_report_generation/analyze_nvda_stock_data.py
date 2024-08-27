# filename: analyze_nvda_stock_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('nvda_stock_data.csv', index_col='Date', parse_dates=True)

# Calculate basic trend by comparing the first and last closing prices
first_price = data['Close'].iloc[0]
last_price = data['Close'].iloc[-1]
trend = "upward" if last_price > first_price else "downward" if last_price < first_price else "stable"

# Calculate mean and median
mean_values = data.mean()
median_values = data.median()

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Close', color=color)
ax1.plot(data.index, data['Close'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Volume', color=color)
ax2.plot(data.index, data['Volume'], color=color, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Nvidia Stock Performance (Close Price and Volume)')
plt.show()

# Printing results
print(f"Trend over the period was {trend}.")
print("\nMean values for each column:")
print(mean_values)
print("\nMedian values for each column:")
print(median_values)