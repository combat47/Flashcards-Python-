# This is Amirhossein Jahazi AKA combat47
def main():
    # Get the number of flashcards
    num_cards = int(input("Input the number of cards:\n"))

    # Initialize a dictionary to store flashcards
    flashcards = {}

    # Create flashcards
    for i in range(1, num_cards + 1):
        term = input(f"The term for card #{i}:\n")
        definition = input(f"The definition for card #{i}:\n")
        flashcards[term] = definition

    # Test the user on flashcards
    for term, definition in flashcards.items():
        print(f'Print the definition of "{term}":')
        user_answer = input("> ")
        if user_answer == definition:
            print("Correct!")
        else:
            print(f'Wrong. The right answer is "{definition}".')


if __name__ == "__main__":
    main()
