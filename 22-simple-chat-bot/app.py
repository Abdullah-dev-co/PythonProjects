import random
import time

def chatbot():
    greetings = ["Hello!",
    "Hi there!",
    "Hey!",
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Howdy!",
    "What's up?",
    "How's it going?",
    "Nice to see you!",
    "Greetings!",
    "Welcome!",
    "Yo!",
    "Sup?",]

    farewells = [ "Goodbye!",  
    "Bye!",  
    "See you later!",  
    "See you soon!",  
    "Take care!",  
    "Farewell!",  
    "Until next time!",  
    "Catch you later!",  
    "Have a good one!",  
    "Peace out!",  
    "Later!",  
    "So long!",  
    "Bye for now!",  
    "Be well!",  
    "Stay safe!",]
    
    jokes = [ "Why don’t skeletons fight each other? They don’t have the guts!",  
    "What do you call fake spaghetti? An impasta!",  
    "Why did the scarecrow win an award? Because he was outstanding in his field!",  
    "How do you organize a space party? You planet!",  
    "Why don’t eggs tell jokes? They’d crack each other up!",  
    "What’s brown and sticky? A stick!",  
    "Why can’t you trust an atom? Because they make up everything!",]

    facts = [
    # Science Facts  
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",  
    "A day on Venus is longer than a year on Venus. It takes Venus 243 Earth days to rotate once, but only 225 Earth days to orbit the Sun.",  
    "The human nose can detect over 1 trillion different scents.",  
    "Octopuses have three hearts, nine brains, and blue blood.",  
    "Bananas are berries, but strawberries aren’t.",  

    # Animal Facts  
    "A group of flamingos is called a 'flamboyance'.",  
    "Crows can recognize human faces and hold grudges against people who have threatened them.",  
    "A shrimp's heart is located in its head.",  
    "Polar bears have black skin under their white fur to better absorb sunlight.",  
    "Koalas have fingerprints almost identical to humans.",  

    # Technology Facts  
    "The first computer virus was created in 1983 and was called the 'Elk Cloner'.",  
    "The first website (info.cern.ch) went live in 1991 and is still online today.",  
    "The average person spends about 6 years of their life on social media.",  
    "The original name of Google was 'Backrub'.",  
    "The '@' symbol in emails was chosen because it was rarely used in computing before email.",  

    # Space Facts  
    "A teaspoon of a neutron star would weigh about 6 billion tons.",  
    "There are more stars in the universe than grains of sand on all Earth’s beaches.",  
    "The footprints on the Moon will last for millions of years because there’s no wind or water to erase them.",  
    "The Sun makes up 99.86% of the mass of our solar system.",  
    "If two pieces of the same type of metal touch in space, they will permanently bond (called 'cold welding').",  

    # Human Body Facts  
    "Your stomach lining regenerates every 3-4 days to prevent it from digesting itself.",  
    "Humans share 50% of their DNA with bananas.",  
    "The strongest muscle in the human body is the masseter (jaw muscle).",  
    "You produce about 25,000 quarts of saliva in your lifetime—enough to fill two swimming pools!",  
    "Your brain can power a light bulb (it generates about 12-25 watts of electricity).",  

    # History Facts  
    "The shortest war in history was between Britain and Zanzibar in 1896—it lasted only 38 minutes.",  
    "Cleopatra lived closer to the invention of the iPhone than to the building of the Great Pyramid.",  
    "The Great Pyramid of Giza was the tallest man-made structure for over 3,800 years.",  
    "In 1923, a jockey won a race despite being dead—he had a heart attack mid-race but his horse crossed the finish line first.",  
    "The Titanic’s distress signals were ignored by a nearby ship because the radio operator was off-duty.",  

    # Fun Random Facts  
    "A single cloud can weigh more than 1 million pounds.",  
    "The inventor of the Pringles can is buried in a Pringles can.",  
    "Scotland has 421 words for 'snow'.",  
    "The shortest scientific paper ever published was just two words long: 'Get lost!'",  
    "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo'.",  
]
    bot_name = "ChatBot"
    print(f"{bot_name} is starting up ...")
    time.sleep(1)

    print(f"""
      Welcom to {bot_name}

      I can chat about:
      'joke' -Hear a funny joke.
      'fact' -Learn something new.
      'color' -My favorite color.
      'bye' -End our chat.
  """)
    
    chatting = True
    user_name = input("Whats your name?").lower().strip()
    print(f"{bot_name}: Nice to meet you, {user_name}! How can I help you today?")

    while chatting:
        user_input = input("You:").lower()
        if user_input in ["hi","hello","hey","howdy"]:
            print(f"{chatbot}: {random.choice(greetings)}")
        elif 'joke'in user_input:
            print(f"{chatbot}: {random.choice(jokes)}")
        elif 'fact'in user_input:
            print(f"{chatbot}: {random.choice(facts)}")
        elif 'color'in user_input:
            print(f"{chatbot}: My favorite color is black! whats yours?")
            color = input("You:").strip()
            print(f"{chatbot}: {color} is a great choice!")
        elif user_input in ["goodbye","bye","exit","quit"]:
            print(f"{chatbot}: {random.choice(farewells)}")
            print(f"It was fun chatting with you, {user_name}")
            chatting = False
        else:
            responses = ["I don’t have information on that topic.",
                         "That’s outside my knowledge base at the moment.",
                         "I can’t assist with that, but I’m great at [other thing]!"]
            print(f"{chatbot}: {random.choice(responses)}")

    print(f"{chatbot}: Thanks for chatting!")


chatbot()