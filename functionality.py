#Anisha Coimbatore, 08/20/2023
# This module used additional functionality as pandas to create a dataframe and show a histogramoutput using seaborn library.

# import pandas, seaborn and matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define function to perform histogram analysis
def perform_histogram_analysis(stock_data, bond_data, save_filename=None):
    stock_df = pd.DataFrame(stock_data, columns=["PURCHASE_ID", "SYMBOL", "NO_SHARES", "PURCHASE_PRICE", "CURRENT_VALUE", "PURCHASE_DATE"])

# Calculate earnings/loss for stock data
    stock_df["Earnings_Loss"] = stock_df["CURRENT_VALUE"] - stock_df["PURCHASE_PRICE"]

# Generate histogram for stock earnings/loss using Seaborn
    plt.figure(figsize=(6, 4))

# Format plot and give lables
    sns.histplot(data=stock_df, x="Earnings_Loss", bins=20, kde=True, color='blue')
    plt.title("Stock Earnings/Loss Histogram")
    plt.xlabel("Earnings/Loss")
    plt.ylabel("Frequency")
    plt.tight_layout()

# Save and display the plot 
    if save_filename:
        plt.savefig(save_filename)
    plt.show()




