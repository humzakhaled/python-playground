# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from art import logo


def deal_card():
    # Returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    # Adds up the cards in the hand
    score = sum(hand)
    
    # If the score is over 21 and there is an Ace (11), change the Ace to a 1
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand) # Recalculate the score with the new 1
        
    return score

def play_blackjack():
    print(logo)
    my_cards = []
    computer_cards = []
    is_finished = False

    # 1. Deal 2 starting cards to both you and the computer
    for _ in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 2. Your Turn
    while not is_finished:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if you lost immediately
        if my_score > 21:
            is_finished = True
        else:
            # Ask if you want another card
            wanna_play = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
            if wanna_play == 'y':
                my_cards.append(deal_card())
            else:
                is_finished = True # You chose to stop

    # 3. Computer's Turn
    # The computer MUST keep drawing until its score is at least 17
    while computer_score < 17 and my_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 4. Final Results
    print(f"\n--- FINAL RESULTS ---")
    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if my_score > 21:
        print("You went over. You lose! 😭")
    elif computer_score > 21:
        print("Computer went over. You win! 😁")
    elif my_score == computer_score:
        print("It's a draw! 🙃")
    elif my_score > computer_score:
        print("You win! 😃")
    else:
        print("You lose! 😤")

# Main program loop
while True:
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if play == 'y':
        play_blackjack()
    else:
        print("Goodbye!")
        break