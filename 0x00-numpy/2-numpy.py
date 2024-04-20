#!usr/bin/python3
"""
Baseball player's BMI
"""
import numpy as np

height_in = [76, 74, 73, 70, 75, 70, 72, 77]
weight_lb = [1.8796, 1.8796, 1.8288, 1.905, 1.905, 1.8542, 1.8730, 1.8910]

# Convert np_height_in from inch to m: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Convert weight_lb from lbs to kg: np_height_m
np_weight_kg = np.array(weight_lb) * 0.453592

bmi = np_weight_kg / np_height_m ** 2
print(bmi)
