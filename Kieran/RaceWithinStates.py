# Imports
import pandas
import matplotlib.pyplot as plt

def openCSV():
    data = pandas.read_csv('police shootings.csv')
    data = data.sort_values(by='date')

    # Creates data frames sepereated into years
    dateData = data[data["date"] > "0000-00-00"]
    return data, dateData

# Creates a 2d array with all 50 states and columns for the totals and races
def createArray(data):
    array = []
    for i in range (50):
        array.append(data["state"].unique().tolist()[i])
    #State, total, asian, white, hispanic/latino, black and other
    array = [[x, 0, 0, 0, 0, 0, 0] for x in array]
    return array

# Counts the race and sort into states
def raceCounter(dataframe, array):
    for _, row in dataframe.iterrows():
        race = row["race"]
        state = row["state"]
        
        # Find the index of the state in the array
        for i, sublist in enumerate(array):
            if sublist[0] == state:
                index = i
                break
        
        array[index][1] += 1
        
        # Increment the corresponding race count based on the value in 'race'
        match race:
            case 'A':
                array[index][2] += 1   
            
            case 'W':
                array[index][3] += 1
            
            case 'H':
                array[index][4] += 1 
                
            case 'N':
                array[index][4] += 1
            
            case 'B':
                array[index][5] += 1
             
            case _:
                array[index][6] += 1
                
    return array

# Gets top 5 states and the different values for races
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
    return state_names, state_values

# Creates the bar charts graph
def barchart(states, stateValues):
    races = ["A", "W", "H/L", "B", "O"]
    
    # Specify the desired window size
    window_width = 12  # Width of the window in inches
    window_height = 6  # Height of the window in inches

    # Create a figure with the specified size
    fig, (graph1, graph2, graph3, graph4, graph5) = plt.subplots(1, 5, figsize=(window_width, window_height))
    
    for graph in [graph1, graph2, graph3, graph4, graph5]:
        graph.set_ylim(0, max(stateValues)+5)

    # Title for the whole figure
    plt.suptitle("")
    
    graph1.set_title(states[0])
    graph2.set_title(states[1])
    graph3.set_title(states[2])
    graph4.set_title(states[3])
    graph5.set_title(states[4])
    
    # Define colors for each bar
    colours = ['blue', 'white', 'red', 'purple', 'orange']

    # Define border color
    border_colour = 'black'

    # Define border width
    border_width = 1
    
    # Plotting
    graph1.bar(races, stateValues[:5], color=colours, edgecolor=border_colour, linewidth=border_width)
    graph2.bar(races, stateValues[5:10], color=colours, edgecolor=border_colour, linewidth=border_width)
    graph3.bar(races, stateValues[10:15], color=colours, edgecolor=border_colour, linewidth=border_width)
    graph4.bar(races, stateValues[15:20], color=colours, edgecolor=border_colour, linewidth=border_width)
    graph5.bar(races, stateValues[20:25], color=colours, edgecolor=border_colour, linewidth=border_width)
    
    # Add labels and title for the whole figure
    fig.text(0.5, 0.01, 'Race', ha='center')
    fig.text(0.005, 0.5, 'No of Deaths', va='center', rotation='vertical')
    
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

def callAllFunctions():
    data, dateData = openCSV()
    stateArray = createArray(data)
    stateArray = raceCounter(dateData, stateArray)
    stateNames, raceValues = sortArray(stateArray)
    barchart(stateNames, raceValues)
    
callAllFunctions()