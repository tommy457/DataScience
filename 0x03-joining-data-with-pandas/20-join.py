#!/usr/bin/python3
"""
Using .melt() to reshape government data

The .melt() method is a handy tool for reshaping data into a useful form.
"""
import pandas as pd
import matplotlib.pyplot as plt


ur_wide = pd.read_csv("ur_wide.csv")

# unpivot everything besides the year column
ur_tall = ur_wide.melt(
    id_vars=['year'],
    var_name='month',
    value_name='unempl_rate'
)

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by='date', ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')

plt.show()
