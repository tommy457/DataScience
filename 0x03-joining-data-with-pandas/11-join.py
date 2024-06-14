#!/usr/bin/python3
"""
Performing an anti join

performed an anti join by first merging the tables with a left join,
selecting the ID of those employees who did not support a top customer,
and then subsetting the original employee's table.
"""
import pandas as pd


employees = pd.read_csv("employees.csv")
top_cust = pd.read_csv("top_cust.csv")

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])
