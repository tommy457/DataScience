#!/usr/bin/python3
"""
Aggregating DataFrames
"""
import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv')

# The head of the sales DataFrame
print(sales.head())

# General info about the sales DataFrame
print(sales.info())

# The mean of weekly_sales
print(sales['weekly_sales'].mean())

# The median of weekly_sales
print(sales['weekly_sales'].median())

# The maximum of the date column
print(sales['date'].max())

# The minimum of the date column
print(sales['date'].min())


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# The IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# The IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[
    ["temperature_c", "fuel_price_usd_per_l", "unemployment"]
].agg(iqr))

# the IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[
    ["temperature_c", "fuel_price_usd_per_l", "unemployment"]
].agg([iqr, np.median]))

# Sort sales by date
sales = sales.sort_values('date')

# The cumulative sum of weekly_sales, add as cum_weekly_sales col
sales['cum_weekly_sales'] = sales['weekly_sales'].cumsum()

# The cumulative max of weekly_sales, add as cum_max_sales col
sales['cum_max_sales'] = sales['weekly_sales'].cummax()
