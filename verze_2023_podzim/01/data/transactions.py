import datetime
import random

import pandas
from faker import Faker

Faker.seed(0)
fake = Faker("en-US")

sender_and_recipient_list = []
for _ in range(100):
    sender_and_recipient_list.append(fake.company())

AVERAGE_TRANSACTION = 10_000

data_without_ids = []
data_with_ids = []

# Initial values
bank_transaction_code = 10_624_661_354
actual_date = datetime.date(2019, 5, 1)

for i in range(1, 1257):
    actual_date += datetime.timedelta(days=random.randint(0, 5))
    amount = round(random.uniform(-AVERAGE_TRANSACTION, AVERAGE_TRANSACTION), 2)
    sender_and_recipient = sender_and_recipient_list[random.randint(0, len(sender_and_recipient_list)) - 1]
    bank_transaction_code += random.randint(1000, 10000)

    for _ in range(0, 2 if i == 2 else int(random.uniform(1, 2.3))):
        if i == 2:
            bank_transaction_code += 123
        sender_and_recipient_description = "sender" if amount > 0 else "recipient"
        data_without_ids.append(
            {"date": actual_date, "amount": amount, sender_and_recipient_description: sender_and_recipient})
        data_with_ids.append(
            {"bank_id": bank_transaction_code,
             "date": actual_date, "amount": amount, sender_and_recipient_description: sender_and_recipient})

df = pandas.DataFrame(data_without_ids)
df.to_json("data_without_ids.json")
df = pandas.DataFrame(data_with_ids)
df.to_json("data_with_ids.json")
