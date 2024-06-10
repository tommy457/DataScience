#!/usr/bin/python3
"""
Avocado supply and demand
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

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(
    x='nb_sold',
    y='avg_price',
    title='Number of avocados sold vs. average price',
    kind='scatter'
)

# Show the plot
plt.show()
