import matplotlib.pyplot as plt
import pandas as pd

def racedate():

    plt.style.use('_mpl-gallery')

    # Read data from file
    data = pd.read_csv('police shootings.csv')

    #Extracting and grouping data
    data['date'] = pd.to_datetime(data['date'])
    data['race'] = data['race'].replace({'H': 'H/N', 'N': 'H/N'}) #Combining data for races H and N
    race_date_incidents = data.groupby([data['date'].dt.year, 'race']).size().unstack(fill_value=0)# Grouping date data into years

    colours = ['blue', 'green', 'red', 'black', 'purple']#sets colours to be used on graph
    plt.figure(figsize=(10, 10))
    
    #Plots Graph of the extracted data and creates axis with names.
    fig, ax = plt.subplots()
    race_date_incidents.plot(kind='bar', stacked=False, color=colours)
    plt.xlabel('Date')
    plt.ylabel('Incidents')
    plt.title('Incidents by Race Over Years') #Creates title of the graph
    plt.legend(title='Race')#Creates key for colours used to display different races
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9) #Alters borders to fit graph and axis in the window.
    fig.set_size_inches(12, 6)
    plt.show()

racedate()