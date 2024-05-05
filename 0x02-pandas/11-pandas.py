#!/use/bin/python3
"""
Slicing and Indexing DataFrames
"""
import pandas as pd


temperatures = pd.read_csv('temperatures.csv')

# Preview temperatures
print(temperatures.head())

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Preview temperatures_ind
print(temperatures_ind.head())

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# A list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subseting temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subseting temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Setting the index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subseting for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sorting temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sorting temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sorting temperatures_ind by country then descending city
print(temperatures_ind.sort_index(
    level=['country', 'city'], ascending=[True, False])
)

# Using Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[
    (temperatures['date'] >= '2010-01-01')
    & (temperatures['date'] <= '2011-12-31')]

# Seting the date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Using .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08':'2011-02'])

# Return the 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22])

# Using slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Using slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Using slicing in both directions at once
print(temperatures.iloc[:5, 2:4])
