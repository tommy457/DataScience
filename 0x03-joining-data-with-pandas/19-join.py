#!/usr/bin/python3
"""
Subsetting rows with .query()

GDP and population data for Australia and Sweden
from the World Bank and expand on it using the .query()
"""
import pandas as pd
import matplotlib.pyplot as plt


gdp = pd.read_csv("gdp.csv")
pop = pd.read_csv("pop.csv")

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(
    gdp,
    pop,
    on=['country', 'date'],
    fill_method='ffill'
)

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()
