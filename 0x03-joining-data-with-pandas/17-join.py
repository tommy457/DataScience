#!/usr/bin/python3
"""
Phillips curve using merge_ordered()
"""
import pandas as pd
import matplotlib.pyplot as plt


inflation = pd.read_csv("inflation.csv")
unemployment = pd.read_csv("sp500.csv")

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(
    inflation,
    unemployment,
    on='date',
    how='inner'
)

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter',
                        x='unemployment_rate',
                        y='cpi',
                        rot='45'
                        )
plt.show()
