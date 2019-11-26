from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('countries.csv')

years_sorted = sorted(set(data.year)) 

for year in years_sorted:
    data_year = data[data.year == year]
    plt.scatter(data_year.gdpPerCapita, data_year.lifeExpectancy, 5)
    plt.title(year)
    plt.xlim(0, 60000)
    plt.ylim(25, 85)
    plt.ylabel('Life Expectancy')
    plt.xlabel('GDP Per Capita')

    plt.savefig(f'scatter_plots/{str(year)}', dpi=300)
    plt.clf()