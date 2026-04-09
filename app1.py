import requests
import matplotlib.pyplot as plt

# User input
symbol = input("Enter crypto: ").lower().strip()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

res = requests.get(url)
data = res.json()
if symbol not in data:
    print("❌ Invalid crypto name")
    exit()
price = data[symbol]['usd']

print(f"Current price of {symbol} is: ${price}")
from datetime import datetime

print("Checked at:", datetime.now())

# Simple graph (dummy past data)
prices = [price-10, price-5, price, price+5]

plt.plot(prices)
plt.title(f"{symbol} Price Trend")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()