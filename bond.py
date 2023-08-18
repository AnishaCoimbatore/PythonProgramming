#Anisha Coimbatore, 08/20/2023
# This module creates a class for bond data

# Import module
from stock import Stock

# Create bond class
class Bond(Stock):
    def __init__(self, purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date, coupon, yield_bond):
        super().__init__(purchase_id, symbol, number_shares, purchase_price, current_cost, purchase_date)
        self.coupon = coupon
        self.yield_bond = yield_bond