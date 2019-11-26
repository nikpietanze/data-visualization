from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('countries.csv')

mean_gdp_per_capita = data.groupby(['country']).mean().gdpPerCapita

top5 = mean_gdp_per_capita.sort_values(ascending=False).head()

kuwait = data[data.country == 'Kuwait']
us = data[data.country == 'United States']

# * GDP & Population Analysis - Kuwait - Absolute
plt.subplot(3, 1, 1)
plt.title('GDP Per Capita')
plt.plot(kuwait.year, kuwait.gdpPerCapita)

plt.subplot(3, 1, 2)
plt.title('GDP in Billions')
plt.plot(kuwait.year, kuwait.population * kuwait.gdpPerCapita / 10**9)

plt.subplot(3, 1, 3)
plt.title('Population in Millions')
plt.plot(kuwait.year, kuwait.population / 10**6)

plt.tight_layout()

plt.show()

# * GDP & Population Analysis - Kuwait - Relative
plt.plot(kuwait.year, kuwait.population / kuwait.population.iloc[0] * 100)

kuwait_gdp = kuwait.population * kuwait.gdpPerCapita

plt.plot(kuwait.year, kuwait_gdp / kuwait_gdp.iloc[0] * 100)
plt.plot(kuwait.year, kuwait.gdpPerCapita / kuwait.gdpPerCapita.iloc[0] * 100)

plt.title('GDP & Population Growth in Kuwait')
plt.legend(['Population', 'GDP', 'GDP Per Capita'])

plt.show()

# * US vs Kuwait
plt.plot(us.year, us.gdpPerCapita)
plt.plot(kuwait.year, kuwait.gdpPerCapita)
plt.legend(['United States', 'Kuwait'])

plt.show()