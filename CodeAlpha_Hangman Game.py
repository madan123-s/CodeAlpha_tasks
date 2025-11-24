import random

# 1. Predefined list of words
words = ["apple", "tiger", "chair", "water", "phone"]

# 2. Select a random word
secret_word = random.choice(words)

# 3. Variables to track progress
guessed_letters = []
incorrect_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# 4. Main game loop
while incorrect_guesses < max_wrong:
    # Show current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", incorrect_guesses, "/", max_wrong)

    # Check if player already won
    if "_" not in display_word:
        print("\n🎉 You guessed the word:", secret_word)
        break

    # Player inputs a guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add guess to guessed list
    guessed_letters.append(guess)

    # Check if correct
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# 5. Game over
if incorrect_guesses == max_wrong:
    print("\n❌ You lost! The word was:", secret_word)