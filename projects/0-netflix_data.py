#!/usr/bin/python3
"""
Analyzing data and creating visualizations for netflix data
"""
import pandas as pd
import matplotlib.pyplot as plt


# import netflix_data.csv file
netflix_df = pd.read_csv('netflix_data.csv')

# Select only data of type Movie
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Select only these colomns
netflix_movies = netflix_subset[
    ['title', 'country', 'genre', 'release_year', 'duration']
]

# Subset movie with more than 60 min in duration
short_movies = netflix_movies[netflix_movies['duration'] < 60]
genre_colors = {
    'Children': 'green',
    'Documentaries': 'red',
    'Stand-Up': 'blue'
}

colors = []
# Iterate over netflix movies and add color to the list depending on genre
for lab, row in netflix_movies.iterrows():
    color = genre_colors.get(row['genre']) or 'Black'
    colors.append(color)

# Create a figure plot
fig, ax = plt.subplots()

# Create a scatter plot
plt.scatter(
    netflix_movies['release_year'],
    netflix_movies['duration'],
    c=colors
)
# Add lable fo x-axies
plt.xlabel('Release year')
# Add lable fo y-axies
plt.ylabel('Duration (min)')
# Add title for the plot
plt.title('Movie Duration by Year of Release')
# Display the plot
plt.show()
