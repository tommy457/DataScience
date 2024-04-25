#!/usr/bin/python3
"""
Boolean logic with numpy and pandas.
"""
import pandas as pd
import numpy as np


cars = pd.read_csv('cars.csv', index_col=0)


# medium: observations with cars_per_cap between 100 and 500

medium = cars[
    np.logical_and(
        cars.loc[:, 'cars_per_cap'] > 100, cars.loc[:, 'cars_per_cap'] < 500
        )
    ]
print(medium)
