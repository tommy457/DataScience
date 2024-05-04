#!/usr/bin/python3
"""
Grouping diffrent columns
"""
import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv')

# Group by type and calculate total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# The proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)

# Preview data
print(sales_propn_by_type)

# Group by type and is_holiday and calculate total weekly sales
sales_by_type_is_holiday = sales.groupby(
    ["type", "is_holiday"]
)["weekly_sales"].sum()

# Preview data
print(sales_by_type_is_holiday)

# For each store type aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg(
    [np.min, np.max, np.mean, np.median]
)

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l
# get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[
    ['unemployment', 'fuel_price_usd_per_l']
].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
