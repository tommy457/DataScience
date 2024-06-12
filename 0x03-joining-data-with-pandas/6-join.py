#!/usr/bin/python3
"""
comparing the results of a left join versus an inner join.
"""
import pandas as pd


toy_story = pd.read_csv("toy_story.csv")
taglines = pd.read_csv("taglines.csv")

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
