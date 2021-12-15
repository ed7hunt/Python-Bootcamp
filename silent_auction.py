from silent_auction_art import logo

print(logo)
print("Welcome to Silent Auction.\n")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    print(bids)
    answer = input("Is there another bidder? Y/N ").upper()
    if answer == "N":
        bidding_finished = True


find_highest_bidder(bidding_record=bids)
