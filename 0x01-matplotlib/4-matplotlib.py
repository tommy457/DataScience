#!/usr/bin/python3
"""
Which avocado size is most popular
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

# Preview dataset
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = (avocados.groupby('size')['nb_sold']).sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(
    x='size',
    y=nb_sold_by_size,
    kind='bar',
    rot='45'
)

# Show the plot
plt.show()
