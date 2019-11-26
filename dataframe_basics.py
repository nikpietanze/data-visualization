from matplotlib import pyplot as plt
import pandas as pd

data = {
    'year': [2008, 2012, 2016],
    'attendees': [112, 321, 729],
    'average age': [24, 43, 31]   
}

#* Build table
df = pd.DataFrame(data)

#* Isolate column
year = df['year']

#* Conditional Isolations
earlier_than_2013 = df['year'] < 2013

#* Display data in a graph
plt.plot(df['year'], df['attendees'])
plt.plot(df['year'], df['average age'])
plt.legend(['attendees', 'average age'])

plt.show()