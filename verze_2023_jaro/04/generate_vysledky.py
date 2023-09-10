from faker import Faker
import random
import pandas
from itertools import permutations

DATA_SIZE = 200
fake = Faker('cs_CZ')
data = []
obory = ("Elektrotechnika", "Informatika", "Technické lyceum")

misto = [f"{i}. místo" for i in range(1, 11)]
souteze_typy = ("fyzikální", "matematická", "zeměpisná", "chemikální", "přírodopisná")
souteze = [f"{i} olympiáda" for i in souteze_typy]
souteze_mista = {}
for i in souteze:
    souteze_mista[i] = []
    for j in misto:
        souteze_mista[i].append(j)

def get_misto_vybrana_soutez(soutez):
    if len(souteze_mista[soutez]) > 0:
        return f"{souteze_mista[soutez].pop(random.randint(0, len(souteze_mista[soutez]) - 1))} ({soutez})"

def get_soutez(row):
    if row["body_mat"] > 70:
        soutez = "matematická olympiáda"
        if random.uniform(0, 1) < 0.025:
            return get_misto_vybrana_soutez(soutez)
    if row["body_mat"] > 65:
        soutez = "fyzikální olympiáda"
        if random.uniform(0, 1) < 0.025:
            return get_misto_vybrana_soutez(soutez)
    if random.uniform(0, 1) < 0.04:
        soutez = random.choice(souteze[2:])
        return get_misto_vybrana_soutez(soutez)
    return ""


def get_obor():
    cislo = random.uniform(0, 1)
    if cislo < 0.5:
        return obory[0]
    elif cislo < 0.7:
        return obory[1]
    else:
        return obory[2]

for _ in range(DATA_SIZE):
    body_prumer = random.gauss(70, 10)
    random_gender = random.uniform(0, 1)
    row = {
        "prijmeni": fake.first_name_male() if random_gender > 0.5 else fake.first_name_female(),
        "krestni_jmeno": fake.last_name_male() if random_gender > 0.5 else fake.last_name_female(),
        "obor": get_obor(),
        "body_aj": int(body_prumer + random.uniform(-10, +15)),
        "body_mat": int(body_prumer + random.uniform(-15, +10)),
        "body_cj": int(body_prumer + random.uniform(-10, +10)),
        "letni_skola": ["ne", "ano"][round(random.uniform(0, 0.6))]
        }
    row["souteze"] = get_soutez(row)
    data.append(row)
    
data = pandas.DataFrame(data)
data.to_csv("04/prijimaci_zkousky.csv", index=False)
