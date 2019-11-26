import pandas as pd
from matplotlib import pyplot as plt

# * Import CSV
data = pd.read_csv('countries.csv')

# * Find Unique Continents
unique_continents = set(data.continent)

# * Isolate data by year
data_2007 = data[data.year == 2007]

# * Isolate data by country
asia_2007 = data_2007[data_2007.continent == 'Asia']
europe_2007 = data_2007[data_2007.continent == 'Europe']

# * Find Mean & Median values
asia_gdp_mean = asia_2007.gdpPerCapita.mean()
asia_gdp_median = asia_2007.gdpPerCapita.median()
europe_gdp_mean = europe_2007.gdpPerCapita.mean()
europe_gdp_median = europe_2007.gdpPerCapita.median()

plt.subplot(2, 1, 1) # subplot(211)
plt.title('Distrobution of GDP Per Capita')
plt.hist(asia_2007.gdpPerCapita, 20, range=(0, 50000), edgecolor='black')
plt.ylabel('Asia')

plt.subplot(2, 1, 2) # subplot(212)
plt.hist(europe_2007.gdpPerCapita, 20, range=(0, 50000), edgecolor='black')
plt.ylabel('Europe')

plt.show()