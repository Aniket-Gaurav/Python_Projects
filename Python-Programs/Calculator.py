# import the os module to use the clear screen function
import os

# define a function to add two numbers
def add_numbers(a, b):
    # return the sum of the two numbers
    return a + b

# define a function to subtract two numbers
def subtract_numbers(a, b):
    # return the difference of the two numbers
    return a - b

# define a function to multiply two numbers
def multiply_numbers(a, b):
    # return the product of the two numbers
    return a * b

# define a function to divide two numbers
def divide_numbers(a, b):
    # return the quotient of the two numbers
    return a / b

# create a dictionary of operations with their corresponding functions
operations = {
    # addition
    "+": add_numbers,
    # subtraction
    "-": subtract_numbers,
    # multiplication
    "*": multiply_numbers,
    # division
    "/": divide_numbers
}

# ask the user for the first number
first_number = float(input("Enter the first number: "))

# print the available operations
print("Available operations:")
for operation in operations:
    # print the operation
    print(operation)

# loop until the user wants to exit
while True:
    # ask the user for the operation
    chosen_operation = input("Pick an operation: ")

    # ask the user for the second number
    second_number = float(input("Enter the second number: "))

    # get the function for the chosen operation
    calculation_function = operations[chosen_operation]

    # perform the calculation
    result = calculation_function(first_number, second_number)

    # print the result
    print(f"{first_number} {chosen_operation} {second_number} = {result}")

    # ask the user if they want to continue
    should_continue = input(
        f"Enter 'y' to continue calculations with {result} or 'n' to exit: "
    ).lower()

    # if the user wants to continue
    if should_continue == "y":
        # set the first number to the result
        first_number = result
        # clear the screen
        os.system('cls')
    else:
        # break out of the loop and exit
        break
