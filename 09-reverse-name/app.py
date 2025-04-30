print("REVERSE NAME GENERATOR ")

while True:
 name = input("\nEnter your name: ")
 if not name:
  break
 reverse_name = name[::-1]
 print(f"Your reversed name is {reverse_name}")
 print(f"In parallel universe they call you {reverse_name.title()}!")

 answer = input("\nDo you want to try again (y/n)?\n")
 if answer != "y":
  break
 