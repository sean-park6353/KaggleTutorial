import pandas as pd


cars = pd.read_csv("./train.csv")

print(cars)
print("1.=============")
print(cars[['country', 'cars_per_cap']])
