#!/usr/bin/python3
"""
Popular genres with right join
"""
import pandas as pd
import matplotlib.pyplot as plt


movie_to_genres = pd.read_csv("movies.csv")
pop_movies = pd.read_csv("action_movies.csv")

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                      left_on='movie_id',
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar', rot='45')
plt.show()
