#!/usr/bin/python3
"""
Correlation between GDP and S&P500

By using the merge_ordered() function,
we were able to fill in the missing data from 2019.
Finally, the correlation of 0.21 between the GDP and S&P500
is low to moderate at best.
"""

import pandas as pd


gdp = pd.read_csv("gdp.csv")
sp500 = pd.read_csv("sp500.csv")

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())
