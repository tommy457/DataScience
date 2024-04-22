#!/usr/bin/python3
"""
Access data with loc in dataFrames.
"""
import pandas as pd


cars = pd.read_csv('cars.csv', index_col=0)

# O bservation for Japan
print(cars.loc['JPN'])

# Observations for Australia and Russia
print(cars.loc[['AUS', 'RU']])

# drives_right value of Morocco.
print(cars.loc['MOR', 'drives_right'])

# Sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# drives_right column as Series
# drives_right's index in the dataframe is 2
print(cars.iloc[:, 2])

# drives_right column as DataFrame
print(cars.iloc[:, [2]])

# cars_per_cap and drives_right as DataFrame
# drives_right's index in the dataframe is 2 and cars_per_cap is 0
print(cars.iloc[:, [0, 2]])
