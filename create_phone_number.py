#!/usr/bin/env python3.8
# Phone number challenge

def create_phone_number(aList):
    number = "("
    for n in range(3):
        number += str(aList[n])
    number += ") "
    for n in range(3,6):
        number += str(aList[n])
    number += "-"
    for n in range(6,10):
        number += str(aList[n])
    return number

example_list = [1,2,3,4,5,6,7,8,9,0]

phone_number = create_phone_number(example_list)
print(phone_number)
