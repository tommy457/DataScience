#!/usr/bin/python3
"""
Using merge_asof() to study stocks

merge_asof() function is very useful in performing
the fuzzy matching between the timestamps of all the tables.
"""
import pandas as pd
import matplotlib.pyplot as plt


jpm = pd.read_csv("jpm.csv")
wells = pd.read_csv("wells.csv")
bac = pd.read_csv("bac.csv")


# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(
    jpm,
    wells,
    on='date_time',
    suffixes=('', '_wells'),
    direction='nearest'
)

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(
    jpm_wells,
    bac,
    on='date_time',
    suffixes=('_jpm', '_bac'),
    direction='nearest'
)

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()
