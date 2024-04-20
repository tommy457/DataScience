#!/usr/bin/python3
"""
2D NumPy Arrays Arithmetic
"""
import numpy as np


baseball = [[180, 78.4, 22.99],
            [215, 102.7, 34.69],
            [210, 98.5, 30.78],
            [188, 75.2, 25.19]]

np_updated = [[1.2303559, -11.16224898, 1],
              [1.02614252, 16.09732309, 1],
              [1.1544228, 5.08167641, 1],
              [0.99484223, 8.14402711, 1]]

np_baseball = np.array(baseball)

# The addition of np_baseball and updated
print(np_baseball + np_updated)

conversion = np.array([0.0254, 0.453592, 1])

# The product of np_baseball and conversion
print(np_baseball * conversion)
