import random

def hangman():
    # List of words
    words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry', 'fig', 'grape']

    # Select a random word
    word = random.choice(words)

    # Initialize variables
    guessed_letters = []
    tries = 6

    # Main game loop
    while tries > 0:
        # Display the current state of the word
        display_word = ''.join([letter + ' ' if letter in guessed_letters else '_ ' for letter in word])
        print(display_word)

        # Prompt the player for a guess
        guess = input("Enter a letter: ").lower()

        # Check if the guess is valid (single letter)
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        # Check if the guess has already been made
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            tries -= 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you've won!")
            break

    # Check if the player has lost
    if tries == 0:
        print("You've run out of tries. The word was:", word)

# Start the game
hangman()
