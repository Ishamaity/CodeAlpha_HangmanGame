import random


# Predefined words for the game
WORDS = [
    "python",
    "computer",
    "coding",
    "program",
    "developer"
]

MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    """Run one complete Hangman game."""

    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n" + "=" * 45)
    print("             HANGMAN GAME")
    print("=" * 45)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses available.")

    while wrong_guesses < MAX_WRONG_GUESSES:

        # Display current game status
        print("\n" + "-" * 45)
        print("Word:", display_word(word, guessed_letters))

        if guessed_letters:
            print("Used letters:", " ".join(sorted(guessed_letters)))

        print(
            f"Incorrect guesses: "
            f"{wrong_guesses}/{MAX_WRONG_GUESSES}"
        )

        # Check whether the player has won
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word!")
            print(f"The word was: {word}")
            return

        # Get player's guess
        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter exactly one alphabetic letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("⚠️ You have already guessed that letter.")
            continue

        # Store the guess
        guessed_letters.add(guess)

        # Check whether the guess is correct
        if guess in word:
            print("✅ Correct guess!")
        else:
            wrong_guesses += 1
            remaining = MAX_WRONG_GUESSES - wrong_guesses

            print("❌ Incorrect guess!")
            print(f"Remaining incorrect guesses: {remaining}")

    # Game over
    print("\n" + "=" * 45)
    print("             GAME OVER")
    print("=" * 45)
    print(f"The correct word was: {word}")


def main():
    """Start the Hangman game."""
    play_game()


if __name__ == "__main__":
    main()
