#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: 10.13.22
# This program lets you guess a number between 0 and 9


import random


def main_game():
    # defining variables.
    max_number = input("What is the highest guessable number?: ")
    guess_number = input("What is your guess? ")
    random_number = random.randint(1, int(max_number))
    # test if input is valid
    try:
        guess_as_int = int(guess_number)
        print("You entered the integer correctly")
        if guess_number == random_number:
            print("You guessed correctly!")
        else:
            print("The correct number was {}".format(random_number))
            print("You guessed wrong , try again.")
    except:
        print("Invalid input")
    finally:
        print("Thanks for playing :D")


if __name__ == "__main__":
    main_game()
