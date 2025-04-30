import random

print("RANDOM RECIPE GENERATOR ")

proteins = ["chicken","beef","egs","fish","tofu"]
veggies = ["brocoli","carrots","spinach","bell peppers","mushrooms"]
carbs = ["rice","pasta","potatos","quinoa","bread"]
methods = ["baked","grilled","roasted","stir-fried"]
flavors = ["garlic","lemon","spicy","herb","sweet & sour"]

while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor= random.choice(flavors)
    print(f"Your random reciope is {flavor} {method} {protein} with {veggie} and {carb}.")
    
    if not input("\nWant to generate another recipe (y/n)?\n").lower().startswith('y'):
        print("\nGoodbye!")
        break