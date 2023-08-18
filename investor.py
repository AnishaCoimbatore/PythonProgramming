#Anisha Coimbatore, 08/20/2023
# This module creates a class for investor and defines output tables for stocks, bond and investor data.

# Import modules 
from stock import Stock
from bond import Bond

# Import tabulate
from tabulate import tabulate

# Create investor class
class Investor:
    def __init__(self, investor_id, name, address, phone, stock_id, bond_id):
        self.name = name
        self.address = address
        self.phone = phone
        self.stocks = []
        self.bonds = []
        self.investor_id = investor_id
        self.stock_id = stock_id
        self.bond_id = bond_id

    def add_stock(self,  purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date):
        stock = Stock(purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date)
        self.stocks.append(stock)

    def add_bond(self, purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond):
        bond = Bond(purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond)
        self.bonds.append(bond)

    def add_investor(self, investor_id, stock_id, bond_id):
        self.investor_id = investor_id
        self.stock_id = stock_id
        self.bond_id = bond_id

# Define functions to tabulate stock, bond and investor data
    def get_stock_table(self):
        headers = ["Purchase_id", "Symbol", "Quantity", "Earnings/Loss", "Yearly Earning/Loss"]
        data = [[stock.purchase_id, stock.symbol, stock.number_shares, stock.loss_gain(), stock.calc_percent_earning()] for stock in self.stocks]
        return tabulate(data, headers=headers, tablefmt="grid")

    def get_bond_table(self):
        headers = ["Purchase_id", "Symbol", "Number_Shares", "Purchase_Price", "Current_Cost", "Purchase_Date", "Coupon", "Yield_Bond"]
        data = [[bond.purchase_id, bond.symbol, bond.number_shares, bond.purchase_price, bond.current_cost, bond.purchase_date, bond.coupon, bond.yield_bond] for bond in self.bonds]
        return tabulate(data, headers=headers, tablefmt="grid")

    def get_investor_table(self):
        headers = ["Investor ID", "Name", "Address", "Phone", "Stock ID", "Bond ID"]
        data = [[self.investor_id, self.name, self.address, self.phone, self.stock_id, self.bond_id]]
        return tabulate(data, headers=headers, tablefmt="grid")

