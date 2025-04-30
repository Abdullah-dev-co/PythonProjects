print("GRADE CALCULATOR ")
scores = []

while True:
    score = input("Enetr a test score or ('done'):\n ")
    if score.lower() =='done':
        print("Goodbye ")
        break

    scores.append(float(score))
    avrage = sum(scores)/len(scores)
    print(f"avrage score: {avrage:.1f}")
    if avrage >= 90:
        print("Grade is A")
    elif avrage >= 80:
        print("Grade is B")
    elif avrage >= 70:
        print("Grade is C")
    else:
        print("You Grade is D or F ")
