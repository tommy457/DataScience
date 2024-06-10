#!/usr/bin/python3
"""
Changes in sales over time
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

# Get the total number of avocados sold on each date
nb_sold_by_date = (avocados.groupby('date')['nb_sold']).sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(
    x='date',
    y=nb_sold_by_date,
    kind='line',
    rot='45'
)

# Show the plot
plt.show()
