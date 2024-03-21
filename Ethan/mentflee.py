#importing packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#function for pie chart
def pie():
    #style for pie chart
    plt.style.use('_mpl-gallery-nogrid')

    # reading data from file
    data = pd.read_csv('police shootings.csv')


    #taking values out of mental illness
    values_column = 'signs_of_mental_illness'
    mentill = data[values_column].sum()
    notmentill = len(data) - mentill

    #finding flee column
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

    #creating colours for pie chart
    colours_flee_notflee = ['#ff9999','#66b3ff']

    # plotting both pie charts
    fig, axs = plt.subplots(1,2,figsize=(10,5))
    #mentally ill pie chart
    axs[0].pie([mentflee, mentnotflee], labels = [f'fleeing\n({mentflee})',f'not fleeing\n({mentnotflee})'], autopct='%1.1f%%', startangle=70, wedgeprops={"linewidth": 1, "edgecolor": "white"}, colors= colours_flee_notflee)

    #altering pie chart size ans setting title
    axs[0].axis('off')
    axs[0].set_aspect('equal')
    axs[0].set_title('mental illness')

    axs[0].tick_params(axis='both', which='major', labelsize=10)

    #not mentally ill
    axs[1].pie([notmentflee, notmentnotflee], labels = [f'fleeing\n({notmentflee})', f'not fleeing\n({notmentnotflee})'], autopct='%1.1f%%', startangle=70, wedgeprops={"linewidth": 1, "edgecolor": "white"}, colors = colours_flee_notflee)

    #aaltering pie chart size and adding title
    axs[1].axis('off')
    axs[1].set_aspect('equal')
    axs[1].set_title('not mental illness')

    axs[1].tick_params(axis='both', which='major', labelsize=10)

    #adding main title
    plt.suptitle('Fleeing vs not fleeing')
    plt.subplots_adjust(top=0.85)

    #displaying pie chart
    plt.show()

pie()

