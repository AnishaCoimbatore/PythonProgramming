#Anisha Coimbatore, 08/20/2023
# This module defines class for stock data and calculated earnings/ losses and percentage earnings/losses

# Import datetime
from datetime import datetime, date 

# Create stock class
class Stock:
    def __init__(self, purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date):
        self.purchase_id = purchase_id
        self.symbol = symbol
        self.number_shares = number_shares
        self.purchase_price = purchase_price
        self.current_cost = current_cost
        self.purchase_date = purchase_date
      
# Calculate earnings/losses
    def loss_gain(self):
        return (self.current_cost - self.purchase_price) * self.number_shares

    def calc_percent_earning(self):
        purchase_date = datetime.strptime(self.purchase_date, '%Y-%m-%d').date()
        days_diff = (date.today() - purchase_date).days
        return (((self.current_cost - self.purchase_price) / self.purchase_price) / (days_diff / 365) * 100)