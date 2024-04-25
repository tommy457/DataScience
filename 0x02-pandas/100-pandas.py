#!/usr/bin/python3
"""
calculate chances of winning a bet.
"""
import numpy as np
import matplotlib.pyplot as plt


all_walks = []
for i in range(500):
    random_walk = [0]

    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)

        elif dice <= 5:
            step = step + 1

        else:
            step = step + np.random.randint(1, 7)

        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t
ends = np_aw_t[-1, :]

# Plot and display histogram
plt.hist(ends)
plt.show()
