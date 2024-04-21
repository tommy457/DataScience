#!/usr/bin/python3
"""
Making a Scatter plot
"""
import matplotlib.pyplot as plt


gdp_cap = [974.5803384, 5937.029525999999, 6223.367465, 4797.231267,
           12779.37964, 34435.367439999995, 36126.4927, 29796.04834,
           1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803,
           12569.85177, 9065.800825, 10680.79282, 1217.032994]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235,
            79.829, 75.635, 64.062, 79.441, 56.728, 65.554,
            74.852, 50.728, 72.39, 73.005, 52.295]

# Scatter plot: gdp_cap on the x-axis, life_exp on the y-axis
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Display the plot
plt.show()
