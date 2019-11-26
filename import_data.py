import pandas as pd
from matplotlib import pyplot as plt

# * Import data from CSV
data = pd.read_csv('countries.csv')

# * Isolate Data
afghanistan = data[data.country == 'Afghanistan']

# * Plot on a graph
plt.plot(afghanistan.year, afghanistan.gdpPerCapita)
plt.title("Afghanistan's GDP Per Capita")

plt.show()