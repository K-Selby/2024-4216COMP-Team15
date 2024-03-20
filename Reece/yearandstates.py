import matplotlib.pyplot as plt
import pandas

plt.style.use('_mpl-gallery')

# Make data:
data = pandas.read.csv('police shootings.csv')
data = data.sort_values(by='date')

#Creates Dataframes, seperated into years:

Year1 = data[data["date"] < "2016-01-00"]
Year2 = data[(data["date"] > "2016-01-00") & (data["date"] < "2017-01-01")]
Year3 = data[(data["date"] > "2017-01-00") & (data["date"] < "2018-01-01")]
Year4 = data[(data["date"] > "2019-01-00") & (data["date"] < "2020-01-01")]
Year5 = data[(data["date"] > "2020-01-00") & (data["date"] < "2021-01-01")]


