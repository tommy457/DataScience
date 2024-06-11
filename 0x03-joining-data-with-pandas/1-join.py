#!/usr/bin/python3
"""
One-to-many relationships
"""
import pandas as pd

licenses = pd.read_csv("licenses.csv")
biz_owners = pd.read_csv("biz_owners.csv")


# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account': 'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# The first few rows of sorted_df
print(sorted_df.head())
