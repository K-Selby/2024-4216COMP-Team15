# Imports
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('police shootings.csv')
data = data.sort_values(by='date')

# Creates data frames sepereated into years
Year1 = data[data["date"] < "2016-01-00"]
Year2 = data[(data["date"] > "2016-01-00") & (data["date"] < "2017-01-01")]
Year3 = data[(data["date"] > "2017-01-00") & (data["date"] < "2018-01-01")]
Year4 = data[(data["date"] > "2019-01-00") & (data["date"] < "2020-01-01")]
Year5 = data[(data["date"] > "2020-01-00") & (data["date"] < "2021-01-01")]

# Creates a 2d array with all 50 states and columns for the totals and races
def CreateArray():
    array = []
    for i in range (50):
        array.append(data["state"].unique().tolist()[i])
    #State, total, asian, white, hispanic, black, latino and other
    array = [[x, 0] for x in array]
    return array

# Counts the race and sort into states
def deathCounter(dataframe, array):
    for _, row in dataframe.iterrows():
       
        state = row["state"]

# Find the index of the state in the array
        for i, sublist in enumerate(array):
            if sublist[0] == state:
                index = i
                break
        
        array[index][1] += 1

    
    return array

# Gets top 5 states
def sortArray(array):
    array = sorted(array, key=lambda x: x[1], reverse=True)
    array = array[:5]
    state_names = []
    state_values = []
    for i in range(5):
        state_names.append(array[i][0])
        state_values.append(array[i][1])
    return state_names, state_values




# Setting up Piechart
def PieChart(StateName, DeathToll, YearNumber): 

    colours = ['#008fd5', '#fc4f30', 'white', '#e5ae37', '#6d904f']

    fig, ax = plt.subplots()

    ax.pie([DeathToll[0], DeathToll[1], DeathToll[2], DeathToll[3], DeathToll[4] ],
    labels = [StateName[0], StateName[1], StateName[2], StateName[3], StateName[4]],
    explode=[0,0,0,0.1,0], 
    colors = colours, 
    autopct='%1.1f%%', 
    startangle=90, 
    wedgeprops={"linewidth": 1, "edgecolor": "black"}, 
    textprops={'fontsize': 8}
    )
    
    fig.canvas.manager.set_window_title(YearNumber)

    fig.set_size_inches(5, 5)
    ax.axis('equal')
    #plt.title("fleeing victims measured by race - Pie Chart")
    plt.show()

#Create Arrays

Array1 = CreateArray()
Array2 = CreateArray()
Array3 = CreateArray()
Array4 = CreateArray()
Array5 = CreateArray()

Array1 = deathCounter(Year1, Array1)
Array2 = deathCounter(Year2, Array2)
Array3 = deathCounter(Year3, Array3)
Array4 = deathCounter(Year4, Array4)
Array5 = deathCounter(Year5, Array5)

Name1, Value1 = sortArray(Array1)
Name2, Value2 = sortArray(Array2)
Name3, Value3 = sortArray(Array3)
Name4, Value4 = sortArray(Array4)
Name5, Value5 = sortArray(Array5)

PieChart(Name1, Value1, "Year 1")
PieChart(Name2, Value2, "Year 2")
PieChart(Name3, Value3, "Year 3")
PieChart(Name4, Value4, "Year 4")
PieChart(Name5, Value5, "Year 5")
