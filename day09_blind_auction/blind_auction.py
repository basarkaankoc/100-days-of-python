import art

print(art.logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for key in bidding_dictionary:
        bid_amount = bidding_dictionary[key]
        if  bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

should_continue = True
bids = {}



while should_continue:
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    add_new = input("Are there any other bidders? Type 'yes or 'no':\n").lower()

    if add_new == "no":
        should_continue=False
        find_highest_bidder(bids)

    elif add_new == "yes":
        print("\n" * 50)
    else:
        should_continue = False
        print("Invalid option. Please type 'yes' or 'no'.")


