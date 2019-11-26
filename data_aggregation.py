import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

data = pd.read_csv('obama.csv', parse_dates=['year_month'])

data_mean = data.groupby('year_month').mean()
data_median = data.groupby('year_month').median()

plt.plot(data_mean.index, data_mean.approve_percent, 'red')
plt.plot(data_median.index, data_median.approve_percent, 'green')
plt.plot(data.year_month, data.approve_percent, 'o', markersize=2, alpha=0.3)
plt.legend(['Mean', 'Median'])


plt.show()