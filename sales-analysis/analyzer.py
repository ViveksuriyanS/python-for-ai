import os
import pandas as pd

# Print current directory
print("Current directory:", os.getcwd())

# Check if data file exists
data_file = "data/sales.csv"
if os.path.exists(data_file):
    print(f"Data file '{data_file}' found.")
else:
    print(f"Data file '{data_file}' not found. Please ensure it is in the current directory.")

# Read the csv file
data_file_csv = "data/sales.csv"
df = pd.read_csv(data_file_csv) 

# Display the first few rows of the dataframe
print("Print the data:")
print(df)
print(f"\n Shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick Operation: Calculate total for each row
df['total'] = df['quantity'] * df['price']
# Display the first few rows of the updated dataframe
print("\nData with Total column:")
print(df)

# craete optput directorory if it does not exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save the updated dataframe to different file formats
# Save as CSV
output_csv = os.path.join(output_dir, "sales_with_total.csv")
df.to_csv(output_csv, index=False)
print(f"\nData saved to {output_csv}")

# Save as Excel
output_excel = os.path.join(output_dir, "sales_with_total.xlsx")
df.to_excel(output_excel, index=False)
print(f"Data saved to {output_excel}")

# Save as JSON
output_json = os.path.join(output_dir, "sales_with_total.json")
df.to_json(output_json, orient='records', lines=True)
print(f"Data saved to {output_json}")   


