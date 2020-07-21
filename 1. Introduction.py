import pylab as pl
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2020]
pop = [2.519, 3.692, 5.263, 6.972, 8.123]
plt.plot(year, pop)
# Adding Axis Labels
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
# Show
plt.show()
