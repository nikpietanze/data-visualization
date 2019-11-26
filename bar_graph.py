import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('countries.csv')

data_2007 = data[data.year == 2007]
top10 = data_2007.sort_values('population', ascending=False).head(10)

x = np.arange(10)

fig, ax1 = plt.subplots()

width = 0.3
plt.xticks(x, top10.country, rotation='vertical')
population = ax1.bar(x, top10.population / 10**6, width)
plt.ylabel('Population')

ax2 = ax1.twinx()
gdp = ax2.bar(x + width, top10.gdpPerCapita * top10.population / 10**9, width, color='orange')
plt.ylabel('GDP')
plt.legend([population, gdp], ['Population in Millions', 'GDP in Billions'])
figure = plt.gcf()
plt.show()