#!/usr/bin/python3
"""
Subsetting 2D NumPy Arrays
"""
import numpy as np


baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

# The 4rd row of np_baseball
print(np_baseball[3])

# Select the entire second column.
np_weight_lb = np_baseball[:, 1]

# The height of 2nd player
print(np_baseball[0: 2])
