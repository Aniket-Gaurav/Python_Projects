# Import necessary libraries
import random
import hangman_stages
import word_list

# Initialize the number of lives a player has
lives = 6

# Randomly select a word from the word list
chosen_word = random.choice(word_list.words)

# Create a display list to show the guessed letters and underscores
display = ['_' for _ in range(len(chosen_word))]

# Print the initial state of the word
print(display)

# Flag to indicate if the game is over
game_over = False

# Main game loop
while not game_over:
    # Get a guessed letter from the player
    guessed_letter = input("Guessed letter: ").lower()

    # Check if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # If the guessed letter is correct, update the display list
        if letter == guessed_letter:
            display[position] = guessed_letter

    # Print the current state of the word
    print(display)

    # If the guessed letter is not in the chosen word, reduce the number of lives
    if guessed_letter not in chosen_word:
        lives -= 1
        # If no lives are left, end the game
        if lives == 0:
            game_over = True
            print("You lose")

    # If there are no more underscores, the player has guessed the word
    if '_' not in display:
        game_over = True
        print("You win")

    # Print the current hangman stage based on remaining lives
    print(hangman_stages.stages[lives])

