#!/usr/bin/python3
"""
adding Labels and ticks to the plot
"""
import matplotlib.pyplot as plt

life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235,
            79.829, 75.635, 64.062, 79.441, 56.728, 65.554,
            74.852, 50.728, 72.39, 73.005, 52.295]
gdp_cap = [974.5803384, 5937.029525999999, 6223.367465, 4797.231267,
           12779.37964, 34435.367439999995, 36126.4927, 29796.04834,
           1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803,
           12569.85177, 9065.800825, 10680.79282, 1217.032994]

# Scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Labels
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Ticks
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

# Add axis ticks
plt.xticks(tick_val, tick_lab)

plt.show()
