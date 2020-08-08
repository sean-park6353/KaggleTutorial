import pandas as pd


l_2d = [

    ["park", "kim", "lee"],
    ["jeesong", "minsoo", "youngpyo"]


]

l_2d_1=[

[123],
    [23]
]
df = pd.DataFrame(l_2d)
# print(df)
df = pd.DataFrame(l_2d,
                  index=[1, 2],
                  columns=[1, 2, 3])
print(df)
