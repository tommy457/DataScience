#!/use/bin/python3
"""
Working with pivot tables
"""
import pandas as pd


temperatures = pd.read_csv('temperatures.csv')

# Adding year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    'avg_temp_c', index=['country', 'city'], columns='year'
)

# Preview the result
print(temp_by_country_city_vs_year)

# Subseting for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subseting for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')])

# Subseting for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[
    ('Egypt', 'Cairo'):('India', 'Delhi'), '2005':'2010'
])

# Return the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filtering for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Return the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filtering for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
