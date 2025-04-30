import random
print("GUESS THE WORD ")

words = ["python","learning","coding","function","reading","fighting"]

while True:
    orignal_word = random.choice(words)
    letters = list(orignal_word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    print(f"\n The word is {scrambled}: ")
    guess = input("Can you guess the word?: ").lower()
    if guess == orignal_word:
        print("You guessed the word correctly")
    else:
        print(f"Wrong! the word was {orignal_word} ")

    if not input("\nWant to try again (y/n)? ").lower().startswith('y'):
        print("\nGoodbye!")
        break

