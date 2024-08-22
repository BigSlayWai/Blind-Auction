import os  
from art import logo
print(logo)

bids = {}
finished_bidding = False

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}")

while not finished_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        finished_bidding = True
        highest_bidder(bids)
    elif should_continue == "yes":
        # Check the operating system and clear the screen accordingly
        if os.name == 'nt':
            os.system('cls')  # Clear screen for Windows
        else:
            os.system('clear')  # Clear screen for macOS and Linux
