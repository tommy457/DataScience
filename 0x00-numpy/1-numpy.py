#!usr/bin/python3
"""
Baseball players' height
"""
import numpy as np


height_in = [76, 74, 73, 70, 75, 70, 72, 77]

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

print(np_height_in)

# Convert np_height_in from inch to m: np_height_m
np_height_m = np_height_in * 0.0254

print(np_height_m)
