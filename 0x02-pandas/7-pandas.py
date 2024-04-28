#!/usr/bin/python3
"""
Sorting rows
"""
import pandas as pd


homelessness = pd.read_csv('homelessness.csv', index_col=0)

# Sorting homelessness in ascending order by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Top few rows
print(homelessness_ind.head())

# Sort homelessness in descending by family_members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

# Top few rows
print(homelessness_fam.head())

# Sort homelessness by region in ascending order
# then descending order by family members
homelessness_reg_fam = homelessness.sort_values(
    ['region', 'family_members'], ascending=[True, False]
)

# Top few rows
print(homelessness_reg_fam.head())
