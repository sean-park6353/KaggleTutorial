import pandas as pd
import re

data = pd.read_csv(
    "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

data.dropna(inplace=True)
dtype_before = type(data['Salary'])
salary_list = data["Salary"].tolist()
print(salary_list)
