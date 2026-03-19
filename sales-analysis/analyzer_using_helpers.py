import pandas as pd
from helpers import calculate_total, format_currency

# Read the csv file
data_file_csv = "data/sales.csv"
df = pd.read_csv(data_file_csv)

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add total column to dataframe
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"Product: {row['product']}, Quantity: {row['quantity']}, Price: {row['price']}, Total: {formatted_total}")

# Show Grand Total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")



