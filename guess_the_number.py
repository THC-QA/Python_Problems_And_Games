#!/usr/bin/env python3.8
# Guess the number

"""Number guessing game calling random library.""" 

from random import randint

def guess(number, target):
    if number < target:
        if (number - target < 5 and number - target > 0) or (target - number < 5 and target - number > 0):
            print("Your guess is low, but pretty close.")
        else:
            print("Your guess is too low.")
    elif number > target:
        if (number - target < 5 and number - target > 0) or (target - number < 5 and target - number > 0):
            print("Your guess is high, but pretty close.")
        else:
            print("Your guess is too high.")
    else:
        print("Congratulations. You guessed correctly.")


loop = True
while loop == True:
    target = randint(0,100)
    print("I'm thinking of a number between 0 and 100.")
    engage = input("Would you like to guess? (Y/N): ")
    if engage == "Y" or engage == "y":
        number = 101
        while number != target:
            number = int(input("Enter your guess, as an integer: "))
            guess(number, target)
        again = input("New number? (Y/N): ")
        if again == "y" or again == "Y":
            continue
        else:
            loop = False
    else:
        loop = False
exit()