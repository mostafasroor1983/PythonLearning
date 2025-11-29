
import pandas as pd
import json
import os

# Read the CSV file

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "sales.csv")
output_csv_path = os.path.join(base_dir, "output", "sales_data.csv")
output_xls_path = os.path.join(base_dir, "output", "sales_data.xlsx")
output_json_path = os.path.join(base_dir, "output", "sales_data.json")

df = pd.read_csv(data_path)
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json(output_json_path, orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel(output_xls_path, index=False)

# 3. Updated CSV (with our new total column)
df.to_csv(output_csv_path, index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")
