bidders = {}
bidding_finished = False

while not bidding_finished:
    while True:
        name = input("What is your name? ").strip()
        if name and not name.isdigit():
            break
        print("Invalid name. Please enter text only.")

    while True:
        try:
            bid = int(input("What is your bid? $"))
            if bid > 0:
                break
            print("Bid must be greater than $0.")
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 50).")

    bidders[name] = bid

    while True:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
        if should_continue in ["yes", "no"]:
            break
        print("Please answer with 'yes' or 'no'.")

    if should_continue == "no":
        bidding_finished = True

highest_bid = 0
winner = ""

for bidder in bidders:
    bid_amount = bidders[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print("\n--- Auction Finished ---")
print(f"The winner is {winner} with a bid amount of ${highest_bid}!")
