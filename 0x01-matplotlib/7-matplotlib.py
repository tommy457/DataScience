#!/usr/bin/python3
"""
Price of conventional vs. organic avocados
"""
import matplotlib.pyplot as plt
import pandas as pd


"""
avocados dataset:

            date          type  year  avg_price         size    nb_sold
0     2015-12-27  conventional  2015       0.95        small  9.627e+06
1     2015-12-20  conventional  2015       0.98        small  8.710e+06
2     2015-12-13  conventional  2015       0.93        small  9.855e+06
3     2015-12-06  conventional  2015       0.89        small  9.405e+06
4     2015-11-29  conventional  2015       0.99        small  8.095e+06
"""

avocados = pd.read_csv('avocados.csv')
# Histogram of conventional and avg_price with 0.5 transparency and 20 bins
avocados[
    avocados["type"] == "conventional"
    ]["avg_price"].hist(alpha=0.5, bins=20)

# Histogram of organic and avg_price with transparency = 0.5 and 20 bins
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
