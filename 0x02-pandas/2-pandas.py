#!/usr/bin/python3
"""
Access data with square brackets in dataFrames.
"""
import pandas as pd


cars = pd.read_csv('cars.csv', index_col=0)

# Country column as Pandas Series
print(cars['country'])

# Country column as Pandas DataFrame
print(cars[['country']])

# DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# First 3 observations
print(cars[:3])

# Fourth, fifth and sixth observation
print(cars[3:6])
