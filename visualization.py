#Anisha Coimbatore, 08/20/2023
# This module uses matplotlib library to plot portfolio value over time

# Import json, scv matplotlib and datetime
import json
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Open and read data from json file
def generate_portfolio_value_chart():
    with open('AllStocks.json') as json_file:  #json file with stocks data
        stock_data_json = json.load(json_file)

# Create dictionaries to store stock prices and portfolio values for each date
    stock_prices = {}
    portfolio_values = {}

    stock_data_csv = []
    with open('Data_Stocks.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            stock_data_csv.append(row)

# Calculate the value of each stock for each date using the closing price from the json file and add exception
    try:
        for purchase_id, symbol, num_shares, purchase_price, current_value, purchase_date in stock_data_csv:
            num_shares = int(num_shares)
            purchase_price = float(purchase_price)
            if symbol not in stock_prices:
                stock_prices[symbol] = {}
            for stock in stock_data_json:
                if stock["Symbol"] == symbol:
                    stock_prices[symbol][stock["Date"]] = stock["Close"]
            if symbol not in portfolio_values:
                portfolio_values[symbol] = {}
            for date, closing_price in stock_prices[symbol].items():
                if date not in portfolio_values[symbol]:
                    portfolio_values[symbol][date] = 0
                portfolio_values[symbol][date] += num_shares * closing_price
    except ValueError as e:
        print("Error: Could not unpack data. Please check the CSV file format.")
        print(e)

# Plot data
    plt.figure(figsize=(10, 6))
    for symbol in stock_prices.keys():
        dates = list(stock_prices[symbol].keys())
        values = [portfolio_values[symbol][date] for date in dates]
        x = [datetime.strptime(date, '%d-%b-%y').date() for date in dates]
        plt.plot(x, values, label=symbol)

# Give headers to plot
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.title('Portfolio Value Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

# Set the x-axis dates
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))


    

