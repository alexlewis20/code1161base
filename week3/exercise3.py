"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
# from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("\nLet\'s set the bounds of the game first:")
    print("What will be the lower bound?")
    lowerBound = not_number_rejector(0)
    print("What will be the upper bound?")
    upperBound = 1
    while lowerBound >= upperBound:
        upperBound = not_number_rejector(0)
        if lowerBound >= upperBound:
            print(
                   "The upper bound can\'t be less than or equal to the lower")
        else:
            print("\nOK then, a number between {} and {}"
                  .format(lowerBound, upperBound))
    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False
    print("\nTime to guess!")
    while not guessed:
        guessedNumber = not_number_rejector(0)
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < lowerBound or guessedNumber > upperBound:
            print("c'mon, that's outside the bounds, try again")
        elif guessedNumber < actualNumber:
            print("Too small, try again ")
        else:
            print("Too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
