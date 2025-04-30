import time

print("COUNTDOWN TIMER ")
print("Countdown form your chosen seconds!")

while True:
 try:
    timer = int(input("Enter seconds to counntdown from: "))
    if timer <= 0:
        print("Please enter positive number!")
        continue
    print(f"Starting countdown from {timer} seconds ")
    for i in range(timer,0,-1):
        print(f"{i} seconds remainig......")
        time.sleep(1)
    print("Countdown completed! ")
    if not input("Do you want to set contdown again (y/n)? ").lower().startswith('y'):
        print("Goodbye!")
        break
 except ValueError:
    print("Please enter number!")

