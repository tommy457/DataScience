#!/usr/bin/python3
"""
Making a histogram plot
"""
import matplotlib.pyplot as plt

life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235,
            79.829, 75.635, 64.062, 79.441, 56.728, 65.554,
            74.852, 50.728, 72.39, 73.005, 52.295]

# histogram plot
plt.hist(life_exp, 5)

# Display the plot
plt.show()
