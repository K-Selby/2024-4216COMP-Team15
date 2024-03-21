import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plt.style.use('_mpl-gallery')

# Read data from file
data = pd.read_csv('police shootings.csv')

data['date'] = pd.to_datetime(data['date'])

race_date_counts = data.groupby([data['date'].dt.year, 'race']).size().unstack(fill_value=0)

colors = ['blue', 'green', 'red', 'black', 'purple', 'yellow']
 
# Plot
race_date_counts.plot(kind='bar', stacked=False, color=colors)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Race Distribution by Date')
plt.legend(title='Race')
plt.show()