#!/usr/bin/python3
"""
Analyzing NYC Public School Test Result Scores
"""
import pandas as pd


# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data columns
print(schools.columns)

# Select only school_name and average_math columns
schools_subset = schools[['school_name', 'average_math']]

# Sort value descending order by average_math.
best_math_schools = schools_subset.sort_values('average_math', ascending=False)

# Calculate total SATs
schools['total_SAT'] = schools['average_math'] \
    + schools['average_writing'] \
    + schools['average_reading']

# Select top 10 schools order by total_SAT
top_10_schools = schools[['school_name', 'total_SAT']]\
    .sort_values('total_SAT', ascending=False)\
    .head(10)

# Preview the result
print(top_10_schools)

# Calculate boroughs
boroughs = schools\
    .groupby('borough')['total_SAT']\
    .agg(['count', 'mean', 'std'])\
    .round(2)

# Get the largest std value
max_value = boroughs['std'].max()

# Get the row associated with the max_value as a DataFrame
largest_std_dev = boroughs[boroughs['std'] == max_value]

columns = {"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"}

# Rename the columns of the DataFrame
largest_std_dev = largest_std_dev.rename(columns=columns)

# Reset the index of the DataFrame
largest_std_dev.reset_index(inplace=True)

# Preview the result
print(largest_std_dev)
