print("CHARACTER TYPE CHECKER ")
char = input('Enter your single character: ')

if char.isalpha():
    print("This is a letter. ")
elif char.isdigit():
    print("This is a digit. ")
else:
    print("Its a special character. ")