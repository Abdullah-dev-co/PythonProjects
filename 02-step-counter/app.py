print("STEP COUNTER: ")

goal = int(input("What is your daily step goal?\n"))
current_steps = int(input("How many steps have you taken today?\n"))
remainig = goal - current_steps

if remainig > 0 :
    print(f"You need {remainig} more steps to reach your goal\n")
elif remainig == 0 :
    print("You have reached your goal!\n")
else:
    print(f"You exceeded your goal by {-remainig} steps!\n")
