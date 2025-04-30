import random

print("WORD SCRAMBLER")

while True:
    word = input("Enter your word to scramble (or 'quit')\n")
    if word.lower() == 'quit':
        print("Goodbye!")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")
    
    