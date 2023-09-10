import random
import datetime
import pandas

product_dict = {"DBR-56": [20, 0.85], "A35-AC": [5, 0.9], "DTC-23": [11, 1.1]}
product_codes = list(product_dict.keys())
month_coefficient = {7: 0.7, 8: 0.8, 11: 1.2, 12: 1.3}

def generate_inventory_movement(num_movements):
    inventory_movement = []
    current_date = datetime.date(2022, 1, 1)
    quantity_dict = {}
    for _ in range(num_movements):
        for product_code in product_codes:
            quantity = quantity_dict.get(product_code, 0)
            average_demand = product_dict.get(product_code)[0]
            if (current_date.day == 1 and current_date.isoweekday() < 6) or (current_date.day == 2 and current_date.isoweekday() == 1) or (current_date.day == 3 and current_date.isoweekday() == 1):
                suppy_coefficient = product_dict.get(product_code)[1]
                received_quantity = int(average_demand * 20 * random.uniform(0.7, 1.2) * suppy_coefficient)
                print(received_quantity)
                quantity += received_quantity
                inventory_movement.append({"date": current_date, "product_code": product_code, "quantity": received_quantity})
            if current_date.weekday() < 5:
                issued_quantity = min(int(random.randint(int(average_demand * 0.5), int(average_demand * 1.5)) * month_coefficient.get(current_date.month, 1)), quantity)
                quantity -= issued_quantity
                inventory_movement.append({"date": current_date, "product_code": product_code, "quantity": - issued_quantity})
            quantity_dict[product_code] = quantity
        current_date += datetime.timedelta(days=1)
    return inventory_movement

# Generate sample inventory movement data
sample_inventory_movement = generate_inventory_movement(365)  # Generate 31 days of movement data for March 2023

df = pandas.DataFrame(sample_inventory_movement)
df.to_csv("01/data/inventory.csv")

