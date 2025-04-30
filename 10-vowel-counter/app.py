print("VOWEL COUNTER ")

while True:
    text = input("\nEnter your text (or 'quit'): ")
    if text.lower() == "quit":
        print("Goodbye!")
        break
    vowels = ["a","e","i","o","u"]
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    print(f"Your text has {count} vowels! ")
    