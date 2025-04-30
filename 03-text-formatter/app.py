print("TEXT FORMATTER:\n")

text = input("Enetr your text: ")
print("1.UPPERCASE")
print("2.lowercase")
print("3.Title Case")
print("4.Sentence case")

choice = input("choose a formate (1-4)\n")

if choice == "1":
 print(text.upper())
if choice == "2":
 print(text.lower())
if choice == "3":
 print(text.title())
if choice == "4":
 print(text.capitalize())
 