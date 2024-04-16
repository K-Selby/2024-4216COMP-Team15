#importing the packages
import matplotlib.pyplot as plt
import pandas as pd 

def pie():
    plt.style .use('_mpl-gallery-nogrid')
    
    #reading data from the file
    data = pd.read_csv("police shootings.csv")

    #collecting the data
    columnValues = 'signs_of_mental_illness'
    mentallyIll = data[columnValues].sum()
    notMentallyIll = len(data) - mentallyIll

    threatLevel = 'threat_level' 

    #setting variables
    threatAttack = (data[threatLevel] == 'attack').sum()
    threatOther = (data[threatLevel] == 'other').sum()
    threatUndetermined = (data[threatLevel] == 'undetermined').sum()

    #differentiating between mentally and not mentally ill
    mentAttack = mentallyIll + threatAttack 
    mentOther = mentallyIll + threatOther 
    mentUndetermined = mentallyIll + threatUndetermined 

    notMentAttack  = notMentallyIll + threatAttack 
    notMentOther = notMentallyIll + threatOther 
    notMentUndetermined = notMentallyIll + threatUndetermined

    #setting the colours for the pie chart 
    colourThreatLevel = ['#f54242', '#4542f5' , '#f5e642']

    #plotting both the pie charts
    fig, axs = plt.subplots(1,2, figsize = (10,5))
    #mentally ill pie chart 
    axs[0].pie([mentAttack, mentOther, mentUndetermined], labels = [f'attack\n', f'other\n', f'undetermined\n'], autopct='%1.1f%%', startangle = 70, wedgeprops = {"linewidth": 1, "edgecolor": "white"}, colors = colourThreatLevel)

    axs[0].axis('off')
    axs[0].set_aspect('equal')
    axs[0].set_title('Mentally Ill')

    axs[0].tick_params(axis = 'both', which = 'major', labelsize = 10)
    #not mentally ill pie chart 
    axs[1].pie([notMentAttack, notMentOther, notMentUndetermined], labels = [f'attack\n', f'other\n', f'undetermined\n'], autopct = '%1.1f%%', startangle = 70, wedgeprops = {"linewidth": 1, "edgecolor": "white"}, colors = colourThreatLevel)

    axs[1].axis('off')
    axs[1].set_aspect('equal')
    axs[1].set_title('Not Mentally Ill')

    axs[1].tick_params(axis = 'both', which = 'major', labelsize = 10)
    #setting the title
    plt.suptitle('Mental Health and Threat Level')
    plt.subplots_adjust(top = 0.85)

    plt.show()

pie()







