import random

# ------------------------------
# Hangman Game
# ------------------------------

# Predefined list of 5 words
word_list = ["python", "apple", "college", "btech", "laptop"]

# Randomly select a word
secret_word = random.choice(word_list)

# Create display list with underscores
display = []
for letter in secret_word:
    display.append("_")

# Game variables
incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("=================================")
print("       🎮 WELCOME TO HANGMAN     ")
print("=================================")
print("You have 6 incorrect guesses.")
print()

# Game loop
while incorrect_guesses < max_attempts and "_" in display:

    print("Word: ", " ".join(display))
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # If guess is correct
    if guess in secret_word:
        print("✅ Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_attempts - incorrect_guesses)
        print()

# Game result
if "_" not in display:
    print("🎉 Congratulations! You won!")
else:
    print("💀 Game Over!")

print("The correct word was:", secret_word)