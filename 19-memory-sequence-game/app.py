import time 
import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

print("\nMEMORY SEQUENCE GAME.")
print("Remember the sequence and type it back.")
print("\nRules: ")
print("- Watch as numbers appear one by one.")
print("- After the sequence is shown, type it back in order.")
print("- Each round adds one more number to remember.")
print("\nHow far can you go?")

input("Press Enter to start.... ")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()
    print(f"=== Round: {current_round} ===")
    print(f"Remember this sequence of {len(sequence)} numbers:")
    
    for number in sequence:
        print(f"\n{number}")
        time.sleep(0.7)
        clear_screen()
        time.sleep(0.3)
    
    print("\nNow repeat the sequence, separated by spaces: ")
    player_answer = input("> ")

    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("Please enter numbers only.")
        game_over = True
        continue
    
    if player_sequence == sequence:
        print(f"Congrats! You remembered all {len(sequence)} numbers.")
        current_round += 1
        time.sleep(1)
    else:
        print(f"Game over! You remembered {current_round-1} numbers.")
        print(f"The correct sequence was {' '.join(str(num) for num in sequence)}")
        game_over = True
        
    if game_over:
        play_again = input("\nDo you want to play again (y/n)? ")
        if play_again.lower().startswith('y'):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing!")
            break
        