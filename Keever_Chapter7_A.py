def main():
    sentences = []
    print("Enter sentences (type 'STOP' to end input):")

    while True:
        sentence = input("Sentence: ")
        if sentence.upper() == "STOP":
            break
        sentences.append(sentence)

    print("\nYou entered the following sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()
