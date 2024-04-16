# Imports
import pandas as pd
import matplotlib.pyplot as plt

def queryDates():
    print("1. To Enter Specific Year (2015-2020)")
    print("2. To Search All Years")
    
    loop = True
    while loop:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                while True:
                    try:
                        inputYear = int(input("Enter Year: "))
                        if 2015 <= inputYear <= 2020:
                            loop = False
                            break
                        else:
                            print("Invalid Year Selection")
                    
                    except ValueError:
                        print("Invalid Option")
            case '2':
                inputYear = 0
                break
            case _:
                print("Invalid Option")
        
    return inputYear

def queryArmed():
    print("1. To Search Records For Armed Deaths")
    print("2. To Search Records For Unarmed Deaths")
    print("3. To Search Records For Both")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'True'
                break
            case '2':
                option = 'False'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
    return option

def queryAge():
    print("1. To Seach Records For A Specific Age (0-100)")
    print("2. To Seach Records For All Ages")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                while True:
                    try:
                        option = int(input("Enter Age: "))
                        option = str(option)
                        break
                    
                    except ValueError:
                        print("Invalid Option")
                        
                return option
            case '2':
                option = 'All'
                break
            case _:
                print("Invalid Option")
                
    return option

def queryGender():
    print("1. To Search Records For Males")
    print("2. To Search Records For Females")
    print("3. To Search Records For Both Genders")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'Male'
                break
            case '2':
                option = 'Female'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
        
    return option

def queryRace():
    print("1. To Search Records For Asian")
    print("2. To Search Records For White")
    print("3. To Search Records For Hispanic/Latino")
    print("4. To Search Records For Black")
    print("5. To Search Records For Other")
    print("6. To Search Records For All Races")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'Asian'
                break
            case '2':
                option = 'White'
                break
            case '3':
                option = 'H/L'
                break
            case '4':
                option = 'Black'
                break
            case '5':
                option = 'Other'
                break
            case '6':
                option = 'All'
                break
            case _:
                print("Invalid Option")
        
    return option

def queryMentalIllness():
    print("1. To Search Records For Those With Signs Of Mental Illness")
    print("2. To Search Records For Those Without Signs Of Mental Illness")
    print("3. To Search Records For Both")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'True'
                break
            case '2':
                option = 'False'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
        
    return option

def queryThreat():
    print("1. To Search Records For Those With Signs Of Being A Threat")
    print("2. To Search Records For Those Without Signs Of Being A Threat")
    print("3. To Search Records For Both")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'True'
                break
            case '2':
                option = 'False'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
        
    return option

def queryFlee():
    print("1. To Search Records For Those Who Were Fleeing")
    print("2. To Search Records For Those Who Were Not Fleeing")
    print("3. To Search Records For Both")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'True'
                break
            case '2':
                option = 'False'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
        
    return option

def queryCamera():
    print("1. To Search Records For Active Body Cameras")
    print("2. To Search Records For Inactive Body Cameras")
    print("3. To Search Records For Both")
    
    while True:
        userInput = input("Enter Option Number: ")
        match userInput:
            case '1':
                option = 'True'
                break
            case '2':
                option = 'False'
                break
            case '3':
                option = 'Both'
                break
            case _:
                print("Invalid Option")
        
    return option

def querySearch():
    year = queryDates()
    age = queryAge()
    armed = queryArmed()
    gender = queryGender()
    race = queryRace()
    menIll = queryMentalIllness()
    threat = queryThreat()
    flee = queryFlee()
    camera = queryCamera()
    
    data = pd.read_csv('police shootings.csv')
    data = data.sort_values(by='date')
    
    if year == 0:
        # Creates data frame
        dataFrame = data[data["date"] > "0000-00-00"]
    else:
        dataFrame = data[(data["date"] > str(year)+"-01-00") & (data["date"] < str(year+1)+"-01-01")]

    if age == 'All':
        dataFrame = dataFrame[dataFrame["age"] > 0]
    else:
        dataFrame = dataFrame[dataFrame["age"] == age]

    if armed == 'True':
        dataFrame = dataFrame[(dataFrame["armed"] != "unarmed") | (dataFrame["armed"] != "")]
    elif armed == 'False':
        dataFrame = dataFrame[(dataFrame["armed"] == "unarmed") | (dataFrame["armed"] == "")]
        
    if gender == 'Male':
        dataFrame = dataFrame[dataFrame["gender"] == "M"]     
    elif gender == 'Female':
        dataFrame = dataFrame[dataFrame["gender"] == "F"]

    if race == 'Asian':
        dataFrame = dataFrame[dataFrame["race"] == "A"]
    elif race == 'White':
        dataFrame = dataFrame[dataFrame["race"] == "W"]
    elif race == 'H/L':
        dataFrame = dataFrame[(dataFrame["race"] == "H") or (dataFrame["race"] == "N")]
    elif race == 'Black':
        dataFrame = dataFrame[dataFrame["race"] == "B"]
    elif race == 'Other':
            dataFrame = dataFrame[(dataFrame["race"] == "O") | (dataFrame["race"] == "")]

    if menIll == 'True':
        dataFrame = dataFrame[dataFrame["signs_of_mental_illness"] == "TRUE"]
    elif menIll == 'False':
        dataFrame = dataFrame[dataFrame["signs_of_mental_illness"] == "FALSE"]

    if threat == 'True':
        dataFrame = dataFrame[dataFrame["threat_level"] == "attack"]
    elif threat == 'False':
        dataFrame = dataFrame[(dataFrame["threat_level"] == "other") | (dataFrame["threat_level"] == "undetermined")]

    if flee == 'False':
        dataFrame = dataFrame[dataFrame["flee"] == "Not fleeing"]
    elif flee == 'True':
        dataFrame = dataFrame[(dataFrame["flee"] != "Not fleeing") & (dataFrame["flee"] != "")]
        
    if camera == 'True':
        dataFrame = dataFrame[dataFrame["body_camera"] == "TRUE"]
    elif camera == 'False':
        dataFrame = dataFrame[dataFrame["body_camera"] == "FALSE"]

    print(dataFrame)

while True:
    # User Interaction
    print("Menu")
    print("1. Mental Illness & Fleeing - EB")
    print("2. Fleeing & Race - MD")
    print("3. Race & States - KS")
    print("4. Year & States - RP")
    print("5. Threat Level & Mental Illness - JA")
    print("6. Race & Date - TW")
    print("7. Query Database")
    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have chosen Mental Illness & Fleeing")
            from Ethan import mentflee
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
        case '7':
            print("You have chosen to query the database")
            querySearch()
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")
            