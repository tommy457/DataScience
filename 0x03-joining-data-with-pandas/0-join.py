#!/usr/bin/python3
"""
first inner join
"""
import pandas as pd

taxi_owners = pd.read_csv("taxi_owners.csv")
taxi_veh = pd.read_csv("taxi_veh.csv")

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Print the shape of taxi_own_veh
print('taxi_own_veh table shape:', taxi_own_veh.shape)
