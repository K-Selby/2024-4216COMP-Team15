# Imports
import pandas as pd
import matplotlib.pyplot as plt


# User Interaction
print("Menu")
print("1. Mental Illness & Fleeing - EB")
print("2. Fleeing & Race - MD")
print("3. Race & States - KS")
print("4. Year & States - RP")
print("5. Threat Level & Mental Illness - JA")
print("6. Race & Date - TW")
print("Q. Quit Program")

while True:
    userInput = input("Enter the menu number for the visuallisation you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have chosen Mental Illness & Fleeing")
        case '2':
            print("You have chosen Fleeing & Race")
            from Matthew import RaceAndFleeing
        case '3':
            print("You have chosen Race & States")
            from Kieran import RaceWithinStates
        case '4':
            print("You have chosen Year & States")
            from Reece import yearandstates
        case '5':
            print("You have chosen Threat Level & Mental Illness")
            from Joe import mentThreat
        case '6':
            print("You have chosen Race & Date")
            from Tom import RaceDate
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")
            