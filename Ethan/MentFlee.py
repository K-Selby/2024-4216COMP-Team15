import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pie():
    plt.style.use('_mpl-gallery-nogrid')

    # reading data from file
    data = pd.read_csv(r'C:\Users\ebpro\OneDrive - Liverpool John Moores University\4216 COMP Comp workshop\Repository Destination\2024-4216COMP-Team15-2\Ethan\police shootings.csv')


    #taking values out of mental illness
    values_column = 'signs_of_mental_illness'
    numtrue = data[values_column].sum()
    numfalse = len(data) - numtrue

    #taking values out of fleeing
    fleecol = 'flee'

    #count of not fleeing
    notfleeingcount = (data[fleecol] == 'Not fleeing').sum()

    #count of fleeing
    fleeingcount = ((data[fleecol] == 'Car') | (data[fleecol] == 'Foot') | (data[fleecol] == 'Other')).sum()
    

    # plot
    fig, ax = plt.subplots()
    ax.pie([fleeingcount, notfleeingcount,numtrue, numfalse], labels = ['fleeing','not fleeing','Mentally Ill', 'Not Mentally Ill'], autopct='%1.1f%%', startangle=90)

    #changing sizes of fonts
    plt.setp(ax.get_xticklabels(), fontsize=10)
    plt.setp(ax.get_yticklabels(), fontsize=10)


    ax.axis('equal')
    ax.set_aspect('equal')
    plt.title('mental illness and fleeing statistics')

    plt.subplots_adjust(top=1)

    plt.show()

x = input("how would you like to see the data represented for mentally ill and fleeing?")
if x == "pie":
    pie()

