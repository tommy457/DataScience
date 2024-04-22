#!/usr/bin/python3
"""
Create DataFrame from a Dictionary
"""
import pandas as pd


names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco']
dr = [True, False, False, False, True, True]
cpc = [809, 731, 588, 18, 200, 70]
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR']

my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

# Build DataFrame cars from my_dict
cars = pd.DataFrame(my_dict)
cars.index = row_labels

print(cars)
