cat > data/fetch_data.py <<EOF
import os
import requests
import pandas as pd

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(ticker):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": ticker,
        "interval": "5min",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    data = fetch_stock_data(ticker)
    if data:
        print(data)
EOF
