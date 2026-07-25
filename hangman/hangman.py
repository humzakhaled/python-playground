import random
from hangman_art import logo, stages, word_list

# Setup initial game state
chosen_word = random.choice(word_list)
game_over = False
lives = 6
correct_letters = []
guessed_letters = []

# Welcome message & Logo
print(logo)
print("Welcome to Hangman! Guess the word letter by letter.")
print("---------------------------------------------------\n")

# Initial word blank state
initial_display = ""
for letter in chosen_word:
    initial_display += "_ "
print(f"Word to guess: {initial_display}\n")


while not game_over:
    # Show status summary before asking for input
    print("---------------------------------------------------")
    print(f"Guessed so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    
    guess = input("Please guess a letter: ").lower()
    print()  # Empty line for neat spacing

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter from A-Z.\n")
        continue

    if guess in guessed_letters:
        print(f"⚠️ You have already guessed '{guess}'. Try a different letter!\n")
        continue
    else:
        guessed_letters.append(guess)

    # Build current word display
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter + " "
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    # Feedback for correct guess
    if guess in chosen_word:
        print(f"✅ Great guess! '{guess}' is in the word.")

    print(f"Word: {display}\n")

    # Feedback for wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"❌ '{guess}' is not in the word. Remaining lives: {lives}")
        print(stages[lives])


        if lives == 0:
            game_over = True
            print("---------------------------------------------------")
            print("☠️ YOU LOSE!")
            print(f"The word was: {chosen_word}")

    # Check if player won
    if "_ " not in display:
        game_over = True
        print("---------------------------------------------------")
        print("🎉 YOU WIN! Great job saving the hangman!")