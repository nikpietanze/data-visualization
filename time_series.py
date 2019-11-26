from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('countries.csv')

# * Isolate data by country
us = data[data.country == 'United States']
china = data[data.country == 'China']

# * Set relative population metrics
us_growth = us.population / us.population.iloc[0] * 100
china_growth = china.population / china.population.iloc[0] * 100

# * Create graph
plt.subplot(2, 1, 1)
plt.title('Population Growth')
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['US', 'China'])
plt.ylabel('Absolute (millions)')
plt.xlabel('Year')

plt.subplot(2, 1, 2)
plt.plot(us.year, us_growth)
plt.plot(china.year, china_growth)
plt.legend(['US', 'China'])
plt.ylabel('Relative')
plt.xlabel('Year')

plt.show()