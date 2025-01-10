
# EXERCISE 9: Working with Spreadsheets

# Write a program that:
# reads the provided spreadsheet file "employees.xlsx" (see Download section at the bottom) with the following information/columns: "name", "years of experience", "job title", "date of birth"
# creates a new spreadsheet file "employees_sorted.xlsx" with following info/columns: "name", "years of experience", where the years of experience is sorted in descending order: so the employee name with the most experience in years is on top.

import pandas as pd


# df -> data frame
df = pd.read_excel('ex9/employees.xlsx', sheet_name="Sheet1")
sorted_df = df.sort_values('Years of Experience', ascending=False)
sorted_df.to_excel("ex9/employees_sorted.xlsx")
