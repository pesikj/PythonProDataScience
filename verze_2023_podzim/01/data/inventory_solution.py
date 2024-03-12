import pandas

df = pandas.read_csv("01/data/inventory.csv")
df = df.sort_values(["product_code", "date"])
df["quantity_stock"] = df.groupby("product_code")["quantity_change"].cumsum()
df.to_csv("01/inventory_data.csv", index=False)

