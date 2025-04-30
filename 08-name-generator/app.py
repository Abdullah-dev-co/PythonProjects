import random 
print("NAME GENERATOR ")

first_part = ["Sun","Moon","Fire","Star","Wind","Ice"]
second_part = ["rider","walker","hunter","seeker","singer","keeper"]

count = int(input("How may names do you want?\n"))

for _ in range(count):
    first_name = random.choice(first_part)
    second_name = random.choice(second_part)
    print(f"{first_name}{second_name}")
