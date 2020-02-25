#!/usr/bin/env python3.8
# Password Generator (simple)
from random import choice
import string
password_loop = True
while password_loop == True:
    characters = string.punctuation + string.ascii_letters + string.digits
    pass_length = int(input("How many characters should the password be?: "))
    password = "".join(choice(characters) for x in range(0,pass_length))
    print(password)
    again = input("Generate another password? (Y/N): ")
    if again == "Y" or again == "y":
        continue
    else:
        password_loop = False
exit()