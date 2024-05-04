#!/usr/bin/python3
"""
Counting diffrent columns
"""
import pandas as pd

sales = pd.read_csv('sales.csv')

# Drop duplicate store and type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Drop duplicate store and department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Preview data
print(holiday_dates)

# The number of stores of each type
store_counts = store_types["type"].value_counts()

# Preview data
print(store_counts)

# The proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# The number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)

# Preview data
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(
    sort=True, normalize=True
)

# Preview data
print(dept_props_sorted)
