import random
import os
from guessing_number_logo import logo

ATTEMPTS = {"easy": 10, "hard": 5}

end_of_game = False


def clear():
    return os.system("clear")


def set_difficulty():
    difficulty = ""

    while difficulty not in ATTEMPTS:
        difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")

    return ATTEMPTS[difficulty]


def check_guess(guess, answer):
    if guess == answer:
        return True
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    print("Guess again.")
    return False


def play_game(max_number):
    random_number = random.randint(1, max_number)

    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    remaining_guesses = set_difficulty()

    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if check_guess(guess, random_number):
            print(f"You win! {random_number} was my number.")
            break
        else:
            remaining_guesses -= 1

    if remaining_guesses == 0:
        print(f"You loose! {random_number} was my number.")


while not end_of_game:
    play_game(100)

    another_game = input("Want to play another game (y/n)? ")
    if another_game != "y":
        end_of_game = True

print("Goodbye")
