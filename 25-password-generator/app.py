import random
import string
import time

def generate_password(length,use_uppercase,use_lowercase,use_numbers,use_special):
    chars = ""

    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    if not chars:
        print("Oops! no charactor type selected.using lowercase by default!")
        chars = string.ascii_lowercase
    
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

def check_password_strength(password):
    score = min(len(password)/16,1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_numbers + has_special) / 4.0
    final_score = (score * 6.0) + (variety * 4.0)

    if final_score >= 8.0:
        return "ULTRA STRONG"
    elif final_score >= 6.0:
        return "STRONG"
    elif final_score >= 4.0:
        return "DECENT"
    else:
        print("NEEDS IMPROVEMENT")

def get_yes_no_input(question):
    while True:
        response = input(question + "(y/n): ").lower()
        if response in ["yes","y"]:
            return True
        elif response in ["no","n"]:
            return False
        else:
            print("Please enter 'y' or 'n'. ")

def main():
    print("\n==== PASSWORD GENERATOR ====")
    print("Generate strong and secure passwords with ease!")

    while True:
        try:
            length = int(input("\nEnter password lenth (8-30):"))
            if 8<= length <=30:
                break
            else:
                print("Please enter length between (8-30)")
        except ValueError:
            print("Oops! Please enter a number.")
    
    print("\n Lets customize your password!")
    use_lowercase = get_yes_no_input("Include lowercase letters (a-z)?")
    use_uppercase = get_yes_no_input("Include uppercase letters (A_Z)?")
    use_numbers = get_yes_no_input("Include numbers (0-9)?")
    use_special = get_yes_no_input("Include special charactors (!@#$%^)?")

    print("\nGenerating your password...")
    time.sleep(2)
    password = generate_password(
        length,use_uppercase,use_lowercase,use_numbers,use_special)
    print("\n YOUR NEW PASSWORD:")
    print(f"{password}")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
    if get_yes_no_input("\n Would you like to generate again?"):
        main()
    else:
        print("GOODBYE!")

main()
