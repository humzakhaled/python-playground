import random
from data import data
from art import logo, vs


def compete_between(compare, against):
    print(f"\nCompare A: {compare['name']}, {compare['description']}")
    print(vs)
    print(f"Against B: {against['name']}, {against['description']}\n")


def user_choice():
    while True:
        choice = input("Who has more followers? Type 'a' or 'b': ").strip().lower()
        if choice in ['a', 'b']:
            return choice
        print("Invalid input: Please type 'a' or 'b'.\n")


def compare_results(current_score, choice, compare, against):
    compare_followers = compare['follower_count']
    against_followers = against['follower_count']

    if compare_followers > against_followers:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    
    if choice == correct_answer:
        return current_score + 1
    else:
        return False


def play_game():
    print(logo)
    current_score = 0
    game_should_continue = True
    compare = random.choice(data)

    while game_should_continue:
        against = random.choice(data)
        while compare == against:
            against = random.choice(data)
        
        compete_between(compare, against)

        choice = user_choice()
        result = compare_results(current_score, choice, compare, against)

        print("\n" + "=" * 40)  

        if result is not False:
            current_score = result
            print(f" You're right! Current score: {current_score}.")
            print("=" * 40)
            compare = against
        else:
            print(f" Wrong answer! Final score: {current_score}.")
            print("=" * 40 + "\n")
            game_should_continue = False


play_game()