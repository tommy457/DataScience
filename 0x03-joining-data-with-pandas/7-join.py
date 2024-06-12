#!/usr/bin/python3
"""
Finding unique movies with a right and inner join
"""
import pandas as pd


movies = pd.read_csv("movies.csv")
action_movies = pd.read_csv("action_movies.csv")
scifi_movies = pd.read_csv("scifi_movies.csv")

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(
    scifi_movies,
    on='movie_id',
    how='right',
    suffixes=['_act', '_sci']
)

# Previw the first few rows of action_scifi to see the structure
print(action_scifi.head())

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(
    scifi_only,
    how='inner',
    left_on='id',
    right_on='movie_id'
)

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)
