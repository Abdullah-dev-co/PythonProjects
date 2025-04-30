import random
import time

word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    "food": ["eat", "cook", "tasty", "meal", "restaurant"],
    "music": ["song", "dance", "listen", "band", "rhythm"],
    "book": ["read", "story", "page", "author", "Library"],
    "tree": ["leaf", "green", "forest", "wood", "shade"],
    "car": ["drive", "road", "wheel", "travel", "speed"],   
    "dog": ["pet", "bark", "walk", "loyal", "puppy"]      
}

print("WORD ASSOCIATION GAME")
print("Respond with a related word quickly!")

score = 0
rounds = 0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]
    print(f"\nPrompt word: {prompt.upper()}")
    print("Respond quickly to this prompt!")
    
    start_time = time.time()
    response = input("> ").lower().strip()
    response_time = time.time() - start_time
    
    print(f"Response time: {response_time:.1f} seconds")

    if response in related_words:
        points = max(1, 5 - int(response_time))
        score += points
        print(f"Good association! +{points} points (answered in {response_time:.1f}s)")
    else:
        print(f"Not a common association. Related words are: {', '.join(related_words)}")
    
    rounds += 1 
    print(f"Score: {score}/{rounds * 5} possible points")
    
    play_again = input("Do you want to play again (y/n)? ").lower().strip()
    if not play_again.startswith('y'):
        print(f"\nFinal score: {score}/{rounds * 5}, Thanks for playing!")
        break
    