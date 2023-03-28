import pandas
import random
import datetime
from faker import Faker

Faker.seed(0)
fake = Faker(['cs-CZ', 'de-AT'])

TOTAL_USERS = 30_000
COUNTRIES = ("Czech Republic", "Austria")
AGE_GROUPS = ("18-29", "30-44", "45-60", "60+")
MARKETING_CHANNELS = ("Newspapers or magazine", "Television", "Outdoor", "Social network", "Friend's recommendation")
AVERAGE_SECONDS_CHANGE = 60 * 60 * 24 * 31 / TOTAL_USERS

date = datetime.datetime(2021, 3, 1)
data = []

while date < datetime.datetime(2021, 4, 1):
    if date.day == 17 and faker_index == 'cs-CZ':
        time_change = AVERAGE_SECONDS_CHANGE * 0.4
    elif date.day < 7:
        time_change = AVERAGE_SECONDS_CHANGE * 1.5
    elif date.day < 15:
        time_change = AVERAGE_SECONDS_CHANGE * 1
    elif date.day < 22:
        time_change = AVERAGE_SECONDS_CHANGE * 0.8
    else:
        time_change = AVERAGE_SECONDS_CHANGE * 0.6
    # int(random.uniform(AVERAGE_SECONDS_CHANGE * 0.9, AVERAGE_SECONDS_CHANGE * 1.1))
    date += datetime.timedelta(seconds=time_change)
    if random.uniform(0, 1) < 0.1 and len(data) > 2000:
        data.append(data[random.randint(0, len(data) - 2000)])
    faker_index = 'cs-CZ' if random.uniform(0, 1) < 0.7 else 'de-AT'
    actual_faker = fake[faker_index] if random.uniform(0, 1) < 0.7 else fake[faker_index]
    age_group_random = random.uniform(0, 1)
    if age_group_random < 0.3:
        age_group = AGE_GROUPS[0]
    elif age_group_random < 0.65:
        age_group = AGE_GROUPS[1]
    elif age_group_random < 0.85:
        age_group = AGE_GROUPS[2]
    else:
        age_group = AGE_GROUPS[3]
    marketing_random = random.uniform(0, 1)
    marketing_channel = None
    if age_group == AGE_GROUPS[0] and marketing_random < 0.4:
        marketing_channel = MARKETING_CHANNELS[3]
    if age_group == AGE_GROUPS[1] and marketing_random < 0.35:
        marketing_channel = MARKETING_CHANNELS[3]
    if age_group == AGE_GROUPS[2] and marketing_random < 0.3:
        marketing_channel = MARKETING_CHANNELS[2]
    if age_group == AGE_GROUPS[3] and marketing_random < 0.45:
        marketing_channel = MARKETING_CHANNELS[0]
    marketing_random = random.uniform(0, 1)
    if not marketing_channel:
        if marketing_random < 0.15:
            marketing_channel = MARKETING_CHANNELS[0]
        elif marketing_random < 0.35:
            marketing_channel = MARKETING_CHANNELS[1]
        elif marketing_random < 0.50:
            marketing_channel = MARKETING_CHANNELS[2]
        elif marketing_random < 0.75:
            marketing_channel = MARKETING_CHANNELS[3]
        else:
            marketing_channel = MARKETING_CHANNELS[4]
    row = {
        "date_time": str(date),
        "email": actual_faker.email(),
        "ip_address": fake.ipv4_public(),
        "age_group": age_group,
        "marketing_channel": marketing_channel
    }
    data.append(row)

df = pandas.DataFrame(data)
df.to_json("user_registration.json")
