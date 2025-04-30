import random

print("GUESS THE NUMBER ")
print("I am guessing a number b/w 1 and 100. You have 10 attempts. ")

playing = True
while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    game_over = False
    while attempts < max_attempts and not game_over:
        try:
            guess = int(input(f"Attempts {attempts + 1}/{max_attempts} guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1 
        
        if guess < secret_number:
            print("The guess is too low, try a higher number")
        elif guess > secret_number:
            print("The guess is too high, try a lower number")
        else:
            print(f"Congrats! You guessed the number {secret_number} in {attempts} attempts!")
            game_over = True
        
        if attempts < max_attempts and not game_over: 
            print(f"You have {max_attempts - attempts} attempts left")
        elif attempts >= max_attempts and not game_over:
            print(f"Game over! The number was {secret_number}")
            game_over = True
    
    play_again = input("Do you want to play again (y/n)? ")
    if play_again.lower().startswith('y'):
        print("New game starting...")
    else:
        print("Goodbye!")
        playing = False