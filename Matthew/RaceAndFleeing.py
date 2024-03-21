import matplotlib.pyplot as plt
import pandas as pd

def raceAndFleeingPieChart():
       plt.style.use('_mpl-gallery-nogrid')
       data = pd.read_csv('police shootings.csv')

       asian, black, hispanic, notHispanic, white, other, unknown = 0, 0, 0, 0, 0, 0, 0

       for _, row in data.iterrows():
              race = row["race"]
              fleeing = row["flee"]
              match race:
                     case "A":
                            if fleeing != "Not fleeing":
                                   asian+=1
                     case "B":
                            if fleeing != "Not fleeing":
                                   black+=1
                     case "H":
                            if fleeing != "Not fleeing":
                                   hispanic+=1
                     case "N":
                            if fleeing != "Not fleeing":
                                   notHispanic+=1
                     case "W":
                            if fleeing != "Not fleeing":
                                   white+=1
                     case "O":
                            if fleeing != "Not fleeing":
                                   other+=1
                     case _:
                            if fleeing != "Not fleeing":
                                   unknown+=1

       colours = ['#008fd5', '#fc4f30', '#d3d3d3', '#e5ae37', '#6d904f']

       fig, ax = plt.subplots()

       ax.pie([black, hispanic, white, other+asian+notHispanic, unknown], 
              labels = [(f'Black\n{black}'),(f'Hispanic\n{hispanic}'), (f'White\n{white}'), (f'Other/Asian\n{other+asian+notHispanic}'), (f'Unknown\n{unknown}')], 
              explode=[0,0,0,0.1,0], 
              colors = colours, 
              autopct='%1.1f%%', 
              startangle=90, 
              wedgeprops={"linewidth": 1, "edgecolor": "white"}, 
              textprops={'fontsize': 8}
              )

       fig.set_size_inches(6, 5.5)
       ax.axis('equal')
       plt.title("fleeing victims measured by race - Pie Chart")
       plt.subplots_adjust(top=0.85)
       plt.show()

raceAndFleeingPieChart()