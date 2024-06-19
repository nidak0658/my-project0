import requests
import pandas as pd

# Your Alpha Vantage API key
API_KEY = 'your_alpha_vantage_api_key'

# Base URL for Alpha Vantage
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def add_stock(symbol, shares):
    portfolio[symbol] = shares

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get('Time Series (1min)')
    if time_series:
        latest_timestamp = list(time_series.keys())[0]
        latest_data = time_series[latest_timestamp]
        return float(latest_data['1. open'])
    return None

def calculate_portfolio_value():
    total_value = 0.0
    for symbol, shares in portfolio.items():
        price = get_stock_data(symbol)
        if price:
            total_value += price * shares
    return total_value

def display_portfolio():
    print("\nYour Portfolio:")
    for symbol, shares in portfolio.items():
        price = get_stock_data(symbol)
        if price:
            print(f"{symbol}: {shares} shares @ ${price:.2f} each")
        else:
            print(f"{symbol}: {shares} shares (price data not available)")
    total_value = calculate_portfolio_value()
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        print("Stock Portfolio Tracking Tool")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
