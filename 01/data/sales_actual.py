import random
import pandas
import datetime
from faker import Faker
from sales_plan import AVERAGE_MONTH_SALES

START_YEAR = 2021
SALES_MANAGERS_COUNT = 5
average_sales = AVERAGE_MONTH_SALES / 25

Faker.seed(0)
fake = Faker(['en-US', 'fr-FR', 'fr-CA', 'ja-JP', 'nl-NL', 'it_IT', 'en-GB'])
sales_managers = [f"{fake['en-GB'].last_name()} {fake['en-GB'].first_name()}" for _ in range(0, SALES_MANAGERS_COUNT)]

year_coefficients = {2021: 1, 2022: 1.3, 2023: 1.2}
months_coefficients = {7: 0.7, 8: 0.8, 10: 1.2, 11: 1.3}

def get_faker():
    random_number = random.random()
    if random_number < 0.2:
        return f"{fake['en-GB'].company()} {fake['en-GB'].company_suffix()}", "United Kingdom"
    elif random_number < 0.3:
        return f"{fake['nl-NL'].company()} {fake['nl-NL'].company_suffix()}", "Netherlands"
    elif random_number < 0.5:
        return f"{fake['fr-FR'].company()} {fake['fr-FR'].company_suffix()}", "France"
    elif random_number < 0.7:
        return f"{fake['fr-CA'].company()} {fake['fr-CA'].company_suffix()}", "Canada"
    elif random_number < 0.9:
        return f"{fake['it-IT'].company()} {fake['it-IT'].company_suffix()}", "Italy"
    else:
        return fake['en-US'].company(), "USA"


def get_sales_manager(country):
    random_number = random.random()
    if random_number < 0.2 and country in ("United Kingdom", "USA"):
        return sales_managers[0]
    elif random_number < 0.5 and country in ("France", "Italy", "Netherlands"):
        return sales_managers[1]
    elif random_number < 0.9 and country in ("Italy", "Canada", "France", "Netherlands"):
        return sales_managers[2]
    else:
        return sales_managers[3]


def generate_data():
    sales = []
    date = datetime.datetime(2021, 1, 1)
    while date < date.today():
        date += datetime.timedelta(days=1)
        if date.isoweekday() in (6, 7):
            continue
        company, country = get_faker()
        row = {
            "date": date,
            "company": company,
            "country": country,
            "contract_value": float(random.randint(int(average_sales * 0.2), int(average_sales * 1.8)))
                              * year_coefficients.get(date.year, 1),
            "sales_manager": get_sales_manager(country)
        }
        sales.append(row)

    df = pandas.DataFrame(sales)
    df = df.sort_values(["country", "company"])
    df.to_csv("sales_actual.csv", index=False)


generate_data()

