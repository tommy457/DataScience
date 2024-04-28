#!/usr/bin/python3
"""
Inspecting a DataFrame with methods and attributes.
"""
import pandas as pd


homelessness = pd.read_csv('homelessness.csv', index_col=0)

# The head of the homelessness data
print(homelessness.head())

# Information about homelessness
print(homelessness.info())

# Description of homelessness
print(homelessness.describe())


# The shape of homelessness
print(homelessness.shape)

# The values of homelessness
print(homelessness.values)

# The column index of homelessness
print(homelessness.columns)

# The row index of homelessness
print(homelessness.index)
