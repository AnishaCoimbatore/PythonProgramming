#Anisha Coimbatore, 08/20/2023
"""WEEK 10 PORTFOLIO PROGRAMMING ASSIGNMENT - IMPROVING THE STOCK PROBLEM WITH ADDITIONAL FUNCTIONALITY
This is the main program file that creates database for stock, bond and investor information and uses the other modules
to import data and display the output. The final output is the stocks data with earnings/losses, bonds data and investor 
information in a tabular format and also displays and saves graphs for portfolio value over time and histogram analysis.
"""

# Import tabulate, datetime, os, sqlite3, csv and matplotlib
from tabulate import tabulate
from datetime import datetime
import os
import sqlite3
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import modules
from investor import Investor
from stock import Stock
from bond import Bond
from visualization import generate_portfolio_value_chart
from functionality import perform_histogram_analysis

# Create a connection to the database and a cursor
def create_database():
    try:
        connection = sqlite3.connect('investment_data.db')
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            purchase_id INTEGER PRIMARY KEY,
            symbol TEXT,
            number_shares INTEGER,
            purchase_price REAL,
            current_cost REAL,
            purchase_date DATE
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS bond (
            purchase_id INTEGER PRIMARY KEY,
            symbol TEXT,
            number_shares INTEGER,
            purchase_price REAL,
            current_cost REAL,
            purchase_date DATE,
            coupon REAL,
            yield_bond REAL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS investor (
            investor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone TEXT,
            stock_id INTEGER,
            bond_id INTEGER,
            FOREIGN KEY (stock_id) REFERENCES stock (purchase_id),
            FOREIGN KEY (bond_id) REFERENCES bond (purchase_id)
        )
        ''')

        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print("Error:", str(e))

# Read data from CSV files and insert into the existing database
def read_csv_insert_database():
    try:
        connection = sqlite3.connect('investment_data.db')
        cursor = connection.cursor()

        with open('Data_Stocks.csv', newline='') as stock_file:
            stock_reader = csv.reader(stock_file)
            next(stock_reader)
            for purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date in stock_reader:
                number_shares = int(number_shares)
                purchase_price = float(purchase_price)
                current_cost = float(current_cost)
                purchase_date = datetime.strptime(purchase_date, '%m/%d/%Y').date()
                cursor.execute('''
                INSERT OR REPLACE INTO stock (purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date))

        with open('bonds_data.csv', newline='') as bond_file:
            bond_reader = csv.reader(bond_file)
            next(bond_reader)
            for purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond in bond_reader:
                number_shares = int(number_shares)
                purchase_price = float(purchase_price)
                current_cost = float(current_cost)
                purchase_date = datetime.strptime(purchase_date, '%m/%d/%Y').date()
                cursor.execute('''
                INSERT OR REPLACE INTO bond (purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond))

        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print("Error:", str(e))

# Read stock data from the database
def retrieve_stock_data_from_db():
    try:
        connection = sqlite3.connect('investment_data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM stock')
        stock_data = cursor.fetchall()

        connection.close()
        return stock_data

    except sqlite3.Error as e:
        print("Error:", str(e))
        return []

# Read bond data from the database
def retrieve_bond_data_from_db():
    try:
        connection = sqlite3.connect('investment_data.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM bond')
        bond_data = cursor.fetchall()

        connection.close()
        return bond_data

    except sqlite3.Error as e:
        print("Error:", str(e))
        return []

# Create tables and insert data into the database
create_database()
read_csv_insert_database()

# Create an investor
investor = Investor("1", "Bunny Coco", "933 Vista", "324-6729-9322", "6", "2")

# Retrieve stock data from the database and add to the investor
stock_data = retrieve_stock_data_from_db()
for stock_info in stock_data:
    investor.add_stock(*stock_info)

# Retrieve bond data from the database and add to the investor
bond_data = retrieve_bond_data_from_db()
for bond_info in bond_data:
    investor.add_bond(*bond_info)

# Print Stock Table
stock_table = investor.get_stock_table()
print("Stock Table:")
print(stock_table)

# Print Bond Table
bond_table = investor.get_bond_table()
print("Bond Table:")
print(bond_table)

# Print Investor Table
investor_table = investor.get_investor_table()
print("Investor Table:")
print(investor_table)

# Generate and save the portfolio value chart
generate_portfolio_value_chart()

# Show and save the plot for portfolio value over time in png format
plt.savefig('portfolio_value_week10.png')

# Save the hsitogram plot in png format
perform_histogram_analysis(stock_data, bond_data, save_filename='stock_earnings_histogram_week10.png')
