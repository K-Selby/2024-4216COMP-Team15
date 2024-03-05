
# User Interaction
print("Menu")
print("1. Mental Illness & Fleeing (Piechart)")
print("2. Fleeing & Race")
print("3. Race & States")
print("4. Year & States")
print("5. Threat Level & Mental Illness")
print("6. ...")

userInput = input("Enter the menu number for the visuallisation you want to view")


match userInput:
    case '1':
        print("You have chosen Mental Illness & Fleeing")
    case '2':
        print("You have chosen Fleeing & Race")
    case '3':
        print("You have chosen Race & States")
    case '4':
        print("You have chosen Year & States")
    case '5':
        print("You have chosen Threat Level & Mental Illness")
    case '6':
        print("You have chosen ...")