from random import randint
from art import logo

# These constants represent the number of turns that the player is given on the easy and hard difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    # Checks answer against guess. Returns the number of turns remaining
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# This function is the main game loop
def game():
    print(logo)
    # Chooses a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    # Repeats the guessing functionality if the user gets it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Lets the user guess a number
        guess = int(input("Make a guess: "))

        # Tracks the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()  # Calls the game() function to start the game
