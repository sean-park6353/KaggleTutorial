import pylab as pl
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

d = {'user': 'bozo', 'pswd': 1234}
print(d['user'])
del(d['user'])
print(d)
d.clear()
print(d)
d['id'] = 45
print(d)
