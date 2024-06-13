#!/usr/bin/python3
"""
Performing an semi join

replicated a semi join to filter the table of tracks
by the table of invoice items to find the top revenue non-musical tracks.
With some additional data manipulation
"""
import pandas as pd


genres = pd.read_csv("genres.csv")
non_mus_tcks = pd.read_csv("non_mus_tcks.csv")
top_invoices = pd.read_csv("top_invoices.csv")

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices)

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres))