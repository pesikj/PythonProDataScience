import random
import pandas

YEARS = (2021, 2022, 2023)
data = []
AVERAGE_MONTH_SALES = 10_000_000

for year in YEARS:
    for month in range(1, 13):
        sales = round(random.uniform(0.8, 1.2) * AVERAGE_MONTH_SALES, -6)
        row = {
            "year": year,
            "month": month,
            "sales": sales
        }
        data.append(row)

df = pandas.DataFrame(data)
df.to_csv("sales_plan.csv", index=False)
