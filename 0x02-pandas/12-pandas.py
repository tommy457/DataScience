#!/use/bin/python3
"""
More Slicing and Indexing DataFrames with loc and iloc
"""
import pandas as pd


temperatures = pd.read_csv('temperatures.csv')

# Setting the index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subseting rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Subseting rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])

# Subseting rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subseting columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subseting in both directions at once
print(temperatures_srt.loc[
    ('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c']
)
