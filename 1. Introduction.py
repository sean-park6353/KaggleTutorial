import pylab as pl
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

raw_data = {
    'first_name': ['park', 'kim', 'lim', np.nan, np.nan],
    'nationality': ['koera', 'korea', 'France', 'UK', 'UK'],
    'age': [28, 23, 25, 36, 70]
}

df = pd.DataFrame(raw_data)

print(df)


df1 = pd.DataFrame(raw_data, columns=['first_name', 'age', 'nationality'])

print(df1)
