#!/usr/bin/python3
"""
Concatenation basics

concatenated set of tables, adjusted the index,
and altered the columns shown in the output.
"""

import pandas as pd

tracks_master = pd.read_csv("tracks_master.csv")
tracks_ride = pd.read_csv("tracks_ride.csv")
tracks_st = pd.read_csv("tracks_st.csv")

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)
