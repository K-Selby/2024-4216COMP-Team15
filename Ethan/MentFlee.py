import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pie():
    plt.style.use('_mpl-gallery-nogrid')

    # reading data from file
    data = pd.read_csv(r'C:\Users\ebpro\OneDrive - Liverpool John Moores University\4216 COMP Comp workshop\Repository Destination\2024-4216COMP-Team15-2\Ethan\police shootings.csv')


    #taking values out of mental illness
    values_column = 'signs_of_mental_illness'
    mentill = data[values_column].sum()
    notmentill = len(data) - numtrue

    #taking values out of fleeing
    fleecol = 'flee'

    #count of not fleeing
    notfleeingcount = (data[fleecol] == 'Not fleeing').sum()

    #count of fleeing
    fleeingcount = ((data[fleecol] == 'Car') | (data[fleecol] == 'Foot') | (data[fleecol] == 'Other')).sum()
    
    #count of mentally ill / fleeing
    mentflee = mentill + fleeingcount

    #count of mentally ill / NOT fleeing
    mentnotflee = mentill + notfleeingcount

    #count of NOT mentally ill / fleeing
    notmentflee = notmentill + fleeingcount

    #count of NOT mentally ill / NOT fleeing
    notmentnotflee = notmentill + notfleeingcount

    # plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.pie([mentflee, mentnotflee,notmentflee, notmentnotflee], labels = ['Mentally ill & fleeing','Mentally ill & not fleeing','Not mentally ill & fleeing', 'Not Mentally Ill & not fleeing'], autopct='%1.1f%%', startangle=90, wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame = True)

    #changing sizes of fonts
    plt.setp(ax.get_xticklabels(), fontsize=10)
    plt.setp(ax.get_yticklabels(), fontsize=10)


    ax.axis('equal')
    ax.set_aspect('equal')
    plt.title('mental illness and fleeing statistics')

    plt.subplots_adjust(top=0.85)

    plt.show()

pie()

