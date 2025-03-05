"""
This program is a number guessing game. The computer thinks of a number between 1 and 50,
and the user has to guess the number. The user can choose the level of difficulty,
which determines the number of attempts the user has to guess the number.
"""

import random


def set_difficulty(level_chosen):
    """
    This function takes in a string representing the level chosen by the user,
    and returns the number of attempts the user has to guess the number.
    """
    if level_chosen == "easy":
        return 10
    elif level_chosen == "medium":
        return 5
    else:
        return 3


def check_answer(guessed_number, answer, attempts):
    """
    This function takes in the user's guessed number, the correct answer, and the number
    of attempts left. It checks if the guessed number is higher or lower than the answer,
    and updates the number of attempts accordingly.
    """
    if guessed_number > answer:
        print("Too high")
        return attempts - 1
    elif guessed_number < answer:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it! {answer} is the answer.")
        return attempts


def game():
    """
    This is the main game function. It prompts the user to choose a level, thinks of a
    number, and then starts the game loop. The game loop continues until the user guesses
    the number correctly or runs out of attempts.
    """
    print("Let me think of a number between 1 and 50.")
    answer = random.randint(1, 50)
    # print(answer)
    level = input("Choose a level: easy, medium, hard: ")
    attempts = set_difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} attempts to guess the number.")
        guessed_number = int(input("Guess the number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:
            print("You are out of guesses ... You lose..")
            return
        elif guessed_number != answer:
            print("Guess again.")


game()
