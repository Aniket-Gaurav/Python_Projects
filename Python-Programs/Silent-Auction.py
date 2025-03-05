import os  # Import the os module to interact with the operating system
print("Welcome to the Silent Auction")  # Print a welcome message for the auction

def find_winner(bidder_details):  # Define a function to find the winner
    highest_bid = 0  # Initialize the highest bid to zero
    winner = ""  # Initialize the winner's name as an empty string
    for bidder in bidder_details:  # Loop through each bidder
        if bidder_details[bidder] > highest_bid:  # Check if the current bid is higher than the highest bid
            highest_bid = bidder_details[bidder]  # Update the highest bid
            winner = bidder  # Update the winner's name
    print(f"The bids are {bidder_details}")  # Print all bids
    print(f"The winner is {winner} with a bid of {highest_bid}")  # Announce the winner

bidder_data = {}  # Initialize an empty dictionary to store bidder data
end_of_bidding = False  # Flag to control the bidding process

while not end_of_bidding:  # Loop until bidding ends
    name = input("Type your Name?: ")  # Prompt for the bidder's name
    price = int(input("Type your bid?: "))  # Prompt for the bid amount
    bidder_data[name] = price  # Store the bid in the dictionary
    more_bidders = input("Do you want to add more bidders? (yes/no): ")  # Ask if there are more bidders
    if more_bidders.lower() == "no":  # If no more bidders
        end_of_bidding = True  # Set the flag to end bidding
        find_winner(bidder_data)  # Call the function to find and announce the winner
    elif more_bidders.lower() == "yes":  # If there are more bidders
        os.system("cls")  # Clear the console screen