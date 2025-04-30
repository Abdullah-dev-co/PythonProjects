import random

print("COIN FLIP GAME ")

while True:
    guess = input("Guess ('heads'or 'tails')\n").lower()
    if guess != 'heads' and guess != 'tails':
        print("Please eneter 'heads'or 'tails'\n")
        continue

    flip = random.choice(['heads','tails'])
    print(f"Coin shows {flip}")
    if guess == flip :
        print("You guessed correctly\n")
    else:
        print("You gussed wrong please try again\n")
    again = input("Play again (yes/no)?\n")   
    if not again.lower().startswith('y'):
        print("Goodbye!") 
        break
    