#!/usr/bin/python3
"""
Lightweight baseball players
"""
import numpy as np

height_in = [76, 74, 73, 70, 75, 70, 72, 77]
weight_lb = [1.8796, 1.8796, 1.8288, 1.905, 1.905, 1.8542, 1.8730, 1.8910]

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light mask array of boolean values
light = bmi < 21
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
# using light as a mask
print(bmi[light])
