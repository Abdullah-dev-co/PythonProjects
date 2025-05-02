import random
import time

def display_welcome():
    print("=== WELCOME TO THE ROCK-PAPER-SCISSORS GAME! ===")
    print("\nPlay 3 rounds to determine the winner!")
    print("------------------------------------------")

def get_user_choice():
    while True:
        print("\nMake a choice: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        try:
            choice = int(input("Enter choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid choice (1-3)")
        except ValueError:
            print("Your choice is invalid. Choose between (1-3)")

def get_computer_choice():
    return random.randint(1, 3)

def convert_choice_to_text(choice):
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return options[choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif ((user_choice == 1 and computer_choice == 3) or
          (user_choice == 3 and computer_choice == 2) or
          (user_choice == 2 and computer_choice == 1)):
        return "user"
    else:
        return "computer"

def display_round_result(user_choice, computer_choice, result):
    user_text = convert_choice_to_text(user_choice)
    computer_text = convert_choice_to_text(computer_choice)
    
    print(f"\nYou chose {user_text}")
    print("Computer is choosing", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(f"\nComputer chose {computer_text}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    display_welcome()
    user_score = 0
    computer_score = 0
    
    for round_num in range(1, 4): 
        print(f"\n=== Round {round_num} ===")
        print(f"Current Score: You {user_score} - {computer_score} Computer")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_round_result(user_choice, computer_choice, result)
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        time.sleep(1) 
    
    print("\n=== GAME OVER ===")
    print(f"Final Score: You {user_score} - {computer_score} Computer")
    
    if user_score > computer_score:
        print("🎉 You won the game! 🎉")
    elif user_score < computer_score:
        print("😢 Computer won the game. 😢")
    else:
        print("🤝 It's a tie! 🤝")
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again.startswith('y'):
        play_game()
    else:
        print("Thanks for playing!")
    
if __name__ == "__main__":
    play_game()

