def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y): 
    return x * y

def division(x, y):
    if y == 0: 
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    print("SIMPLE CALCULATOR") 
    print("Choose operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("\nEnter choice (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid choice!")
        else:
            break
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        return
    
    if choice == '1':
        result = addition(num1, num2)
        print(f"\n{num1} + {num2} = {result}")  
    elif choice == '2':
        result = subtraction(num1, num2)
        print(f"\n{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiplication(num1, num2)
        print(f"\n{num1} x {num2} = {result}")  
    elif choice == '4':
        result = division(num1, num2)
        print(f"\n{num1} / {num2} = {result}")
    
    again = input("\nDo you want to perform another calculation (y/n)? ").lower()
    if not again.startswith('y'):
        print("Goodbye!")
    else:
        main()

main()
        
