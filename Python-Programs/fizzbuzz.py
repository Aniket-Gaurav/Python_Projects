# loop through numbers 1 to 100
for number in range(1, 101):
    # if the number is divisible by 3 and 5, print "fizzbuzz"
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    # if the number is divisible by 3, print "fizz"
    elif number % 3 == 0:
        print("fizz")
    # if the number is divisible by 5, print "buzz"
    elif number % 5 == 0:
        print("buzz")
    # otherwise, just print the number
    else:
        print(number)
