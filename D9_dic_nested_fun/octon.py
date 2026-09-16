print("Welcome to highest bid")


def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ₹{highest_bid}.")


bid_dict = {}
restart = True

while restart:
    your_name = input("What is your name: ")
    bid = int(input("What is your bid: ₹"))
    bid_dict[your_name] = bid

    continues = (
        input("Are there any other bidders? Y for yes and N for no: ")
        .strip()
        .upper()
    )

    if continues == "N":
        restart = False
        find_highest_bidder(bid_dict)
    elif continues == "Y":
        print("\n" * 20)