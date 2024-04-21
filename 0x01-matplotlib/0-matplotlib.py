#!/usr/bin/python3
"""
Making a Line plot
"""
import matplotlib.pyplot as plt


year = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958]
population = [2.53, 2.57, 2.62, 2.67, 2.71, 2.76, 2.81, 2.86, 2.92]

# Line plot: year on the x-axis, pop on the y-axis
plt.plot(year, population)

# Display the plot
plt.show()
