def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text, include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))
    
def count_sentences(text):
    # basic sentence endings:
    sentence_endings = [".", "!", "?"] 
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1

    # handling edge case:
    if count == 0 and text.strip():
        count = 1
    return count


def analyze_text(text):
    word_count = count_words(text)
    count_characters_with_spaces = count_characters(text, True)
    count_characters_without_spaces = count_characters(text, False)
    sentence_count = count_sentences(text)

    if sentence_count > 0:
        words_per_sentence = word_count / sentence_count
    else:
        words_per_sentence = 0
    
    if word_count > 0:
        char_per_words = count_characters_without_spaces / word_count 
    else:
        char_per_words = 0

    print("\n==== Text Analysis Results ====")
    print(f"Words: {word_count}")
    print(f"Characters (with spaces): {count_characters_with_spaces} ")
    print(f"Characters (without spaces): {count_characters_without_spaces}")
    print(f"Sentences: {sentence_count}")
    print(f"Average words per sentence: {words_per_sentence:.1f}")
    print(f"Average characters per word: {char_per_words:.1f}")

    reading_time_minutes = word_count / 225
    if reading_time_minutes < 1:
        reading_time_seconds = reading_time_minutes * 60
        print(f"Estimated reading time: {int(reading_time_seconds)} seconds") 
    else:
        print(f"Estimated reading time: {reading_time_minutes:.1f} minutes")


def main():
    print("\n==== WORD COUNTER ====")
    print("Count words, characters, and sentences in your text")

    while True:
        print("\nChoose options below:")        
        print("1. Analyze text.")        
        print("2. Exit.")  

        choice = input("Your choice (1/2): ")  

        if choice == '1':
            print("Enter or paste your text (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "" and (not lines or lines[-1] == ""):
                    break
                lines.append(line)
            
            text = "\n".join(lines).strip()
            if not text:
                print("No text provided, try again.")
                continue

            analyze_text(text)

        elif choice == '2':
            print("Goodbye!")
            break 
        else:
            print("Invalid choice, try 1 or 2")


if __name__ == "__main__":
    main()