import pandas as pd

print("Sales Columns:")
print(pd.read_csv("sales_promotions.csv").columns.tolist())

print("\nInventory Columns:")
print(pd.read_csv("inventory.csv").columns.tolist())

print("\nProduct Columns:")
print(pd.read_csv("product_master.csv").columns.tolist())

print("\nStore Columns:")
print(pd.read_csv("store_master.csv").columns.tolist())