import pandas as pd
from matplotlib import pyplot as plt

data_big = pd.read_csv('obama_too_big.csv', parse_dates=['year_month'])
data = pd.read_csv('obama.csv', parse_dates=['year_month'])

sampled = data_big.sample(frac=0.1)

plt.plot(sampled.year_month, sampled.approve_percent, 'o', markersize=2, alpha=0.3)

plt.show()