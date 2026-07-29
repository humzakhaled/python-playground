import random
from art import logo

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Get difficulty choice
def difficulty_level():
    while True:
        level = input("Choose difficulty level: 'easy' or 'hard': ").strip().lower()
        if level in ['easy', 'hard']:
            return level
        print("Invalid input. Please type 'easy' or 'hard'.")


# Get turns count
def my_tries(level):
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Compare guess to answer
def check_answer(guess, answer, tries):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return tries
    elif guess > answer:
        print("Too high.")
        return tries - 1
    elif guess < answer:
        print("Too low.")
        return tries - 1


# Main game logic
def make_a_guess():
    print(logo)
    
    answer = random.randint(1, 100)
    level = difficulty_level()
    tries = my_tries(level)

    guess = 0

    while guess != answer and tries > 0:
        print(f"\nYou have {tries} attempts remaining to guess the number.")

        # Input validation
        while True:
            try:
                guess = int(input('Make a guess: '))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            
        # Update remaining tries
        tries = check_answer(guess, answer, tries)
    
    # Game over
    if tries == 0:
        print(f"\n😭 You've run out of guesses! You lose. The number was {answer}.")


make_a_guess()