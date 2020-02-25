#!/usr/bin/env python3.8

# Python Calculator

"""Basic calculator for two number statements, asking user input."""

from math import *

def add_num(num1, num2):
    result = num1 + num2
    return result

def minus_num(num1, num2):
    result = num1 - num2
    return result

def mult_num(num1, num2):
    result = num1 * num2
    return result

def div_num(num1, num2):
    result = num1 / num2
    return result

loop = True
while loop == True:
    print("This is a basic calculator, for two number statements.")
    num1 = float(input("Please input the first number: "))
    operator = input("Please input operator from + - * /: ")
    num2 = float(input("Please input the second number: "))
    if operator == "+":
        answer = add_num(num1, num2)
        print("Problem: " + str(num1) + " " + operator + " " + str(num2))
        print("Answer: ", answer)
    elif operator == "-":
        answer = minus_num(num1, num2)
        print("Problem: " + str(num1) + " " + operator + " " + str(num2))
        print("Answer: ", answer)
    elif operator == "*":
        answer = mult_num(num1, num2)
        print("Problem: " + str(num1) + " " + operator + " " + str(num2))
        print("Answer: ", answer)
    elif operator == "/":
        answer = div_num(num1, num2)
        print("Problem: " + str(num1) + " " + operator + " " + str(num2))
        print("Answer: ", answer)
    else:
        print("Something went wrong. Were your inputs correct?")
    go_again = input("Is there another problem? (Y/N): ")
    if go_again == "y" or go_again == "Y":
        continue
    else:
        loop = False
quit()
