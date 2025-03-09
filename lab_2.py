import pandas as pd
from collections import Counter

data = pd.read_csv("data.csv", sep=";")

print("\nZaładowane dane:")
print(data)

print("\nCharakterystyki podstawowe:")
print(data.describe())

print("\nWartości dla kolumn:")

for x in data:
    print("\ncecha: ", x)

    for key, value in Counter(data[x]).items():
        print(f"{key}: {value}")
