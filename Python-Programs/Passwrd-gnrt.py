# Import the random module to generate random passwords
import random

# Define a list of lowercase letters
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# Define a list of numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Define a list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Print a welcome message
print("Welcome to the PyPassword Generator!")


# Prompt the user to enter the number of letters they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))

# Prompt the user to enter the number of symbols they want in their password
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Prompt the user to enter the number of numbers they want in their password
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty string to store the generated password
password = ""

# Generate the password by randomly selecting characters from the above lists
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# Print the generated password
print(f"Your password is: {password}")

