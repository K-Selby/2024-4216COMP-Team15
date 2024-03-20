# Imports
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('police shootings.csv')
data = data.sort_values(by='date')

# Creates data frames sepereated into years
dateData1 = data[data["date"] < "2016-01-00"]
dateData2 = data[(data["date"] > "2016-01-00") & (data["date"] < "2017-01-01")]
dateData3 = data[(data["date"] > "2017-01-00") & (data["date"] < "2018-01-01")]
dateData4 = data[(data["date"] > "2019-01-00") & (data["date"] < "2020-01-01")]
dateData5 = data[(data["date"] > "2020-01-00") & (data["date"] < "2021-01-01")]

# Creates a 2d array with all 50 states and columns for the totals and races
def createArray():
    array = []
    for i in range (50):
        array.append(data["state"].unique().tolist()[i])
    #Sate, total, asian, white, hispanic, black, latino and other
    array = [[x, 0, 0, 0, 0, 0, 0, 0] for x in array]
    return array

# counts the race and sort into states
def deathCounter(dataframe, array):
    for _, row in dataframe.iterrows():
        race = row["race"]
        state = row["state"]
        
        # Find the index of the state in the array
        for i, sublist in enumerate(array):
            if sublist[0] == state:
                index = i
                break
        
        array[index][1] += 1
        
        # Increment the corresponding race count based on the value of 'race'
        match race:
            case 'A':
                array[index][2] += 1   
            
            case 'W':
                array[index][3] += 1
            
            case 'H':
                array[index][4] += 1 
            
            case 'B':
                array[index][5] += 1
            
            case 'N':
                array[index][6] += 1
            
            case _:
                array[index][7] += 1
                
    return array

# Gets top 5 states
def sortArray(array):
    array = sorted(array, key=lambda x: x[1], reverse=True)
    array = array[:5]
    state_names = []
    state_values = []
    for i in range(5):
        state_names.append(array[i][0])
        state_values.append(array[i][2])
        state_values.append(array[i][3])
        state_values.append(array[i][4])
        state_values.append(array[i][5])
        state_values.append(array[i][6])
        state_values.append(array[i][7])
    return state_names, state_values

# Creates the bar charts graphs
def barchart(states, stateValues):
    races = ["A", "W", "H", "B", "L", "O"]
    
    fig, (graph1, graph2, graph3, graph4, graph5) = plt.subplots(1, 5)
    
    for graph in [graph1, graph2, graph3, graph4, graph5]:
        graph.set_ylim(0, max(stateValues)+5)
    
    graph1.set_title(states[0])
    graph2.set_title(states[1])
    graph3.set_title(states[2])
    graph4.set_title(states[3])
    graph5.set_title(states[4])
    
    # Plotting
    graph1.bar(races, stateValues[:6])
    graph2.bar(races, stateValues[6:12])
    graph3.bar(races, stateValues[12:18])
    graph4.bar(races, stateValues[18:24])
    graph5.bar(races, stateValues[24:30])
 
    plt.show()

yearArray1 = createArray()
yearArray2 = createArray()
yearArray3 = createArray()
yearArray4 = createArray()
yearArray5 = createArray()

yearArray1 = deathCounter(dateData1, yearArray1)
yearArray2 = deathCounter(dateData2, yearArray2)
yearArray3 = deathCounter(dateData3, yearArray3)
yearArray4 = deathCounter(dateData4, yearArray4)
yearArray5 = deathCounter(dateData5, yearArray5)

yearStates1, yearValues1 = sortArray(yearArray1)
yearStates2, yearValues2 = sortArray(yearArray2)
yearStates3, yearValues3 = sortArray(yearArray3)
yearStates4, yearValues4 = sortArray(yearArray4)
yearStates5, yearValues5 = sortArray(yearArray5)

barchart(yearStates1, yearValues1)
barchart(yearStates2, yearValues2)
barchart(yearStates3, yearValues3)
barchart(yearStates4, yearValues4)
barchart(yearStates5, yearValues5)