#!/usr/bin/python3
"""
Removing missing values
"""
import matplotlib.pyplot as plt
import pandas as pd


"""
avocados_2016 dataset:


          date  avg_price  total_sold  small_sold  large_sold    xl_sold  total_bags_sold  small_bags_sold  large_bags_sold  xl_bags_sold
0   2016-12-25       1.00   3.029e+07   9.255e+06   1.028e+07  5.420e+05        1.021e+07        7.710e+06        2.417e+06      81101.22
1   2016-12-18       0.96   2.958e+07   9.394e+06   1.034e+07  4.279e+05        9.423e+06        6.970e+06        2.358e+06      94011.78
2   2016-12-11       0.98   3.009e+07   9.010e+06         NaN  4.030e+05        1.071e+07        8.149e+06        2.490e+06      73342.82
3   2016-12-04       1.00   3.162e+07   1.104e+07   9.909e+06  4.280e+05        1.024e+07        7.187e+06        2.989e+06      65350.63
4   2016-11-27       1.21   2.292e+07   7.891e+06   7.337e+06        NaN        7.350e+06        5.691e+06        1.610e+06      48623.28
5   2016-11-20       1.27   2.499e+07         NaN   8.034e+06  4.076e+05        8.017e+06        6.207e+06        1.766e+06      44709.40
"""

avocados_2016 = pd.read_csv('avocados_2016.csv')

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar', rot='45')

# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
