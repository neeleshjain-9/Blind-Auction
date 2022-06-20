from art import logo
import os

print(logo)
print("Welcome to the secret auction program!!")
bids = {}


def add_to_bid_list(name, bid):
    bids[name] = bid


def winner():
    max = 0
    winner = ""
    for name in bids:
        if bids[name] > max:
            max = bids[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${max}")


while True:
    name = input("What is your name: ")
    bid = int(input("What is your bid? $ "))
    add_to_bid_list(name, bid)

    if input("Are there any other bidders? Type 'yes' to bid, anything else to end: ").lower() == "yes":
        continue
    else:
        break

winner()
