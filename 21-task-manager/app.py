tasks = []

def display_menu():
    print("\n=====TASK MANAGER=====")
    print("1.Add task")
    print("2.View tasks")
    print("3.Complete task")
    print("4.Delete task")
    print("5.Exit")
    print("================================")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ")
        
        
main()