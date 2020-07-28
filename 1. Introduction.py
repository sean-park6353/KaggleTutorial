import pandas as pd


l_1d = ["나는", "가수", "입니다"]
s = pd.Series(l_1d)
print(s)

s = pd.Series(l_1d, index=["1행", "2행", "3행"])

print(s)
