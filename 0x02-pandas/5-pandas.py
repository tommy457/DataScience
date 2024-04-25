#!/usr/bin/python3
"""
Lopping over DataFrames and adding new columns.
"""
import pandas as pd


cars = pd.read_csv('cars.csv', index_col=0)

for lab, row in cars.iterrows():
    print(f"{lab}: {row['cars_per_cap']}")


cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
