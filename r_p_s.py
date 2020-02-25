#!/usr/bin/env python3.8
# Rock, Paper, Scissors
"""A semi-adaptive version of rock, paper, scissors."""
from random import randint
def rps(machine_hand, player_hand):
    if player_hand == "rock":
        if machine_hand == "rock":
            print("It's a tie.")
        elif machine_hand == "paper":
            print("Paper covers rock, you lose.")
        else:
            print("Rock blunts scissors, you win.")
    elif player_hand == "paper":
        if machine_hand == "rock":
            print("Paper covers rock, you win.")
        elif machine_hand == "paper":
            print("It's a tie.")
        else:
            print("Scissors cut paper, you lose.")
    else:
        if machine_hand == "rock":
            print("Rock blunts scissors, you lose.")
        elif machine_hand == "paper":
            print("Scissors cut paper, you win.")
        else:
            print("It's a tie.")
scores = {"rock":1,"paper":2,"scissors":3}
choice = {1:"paper",2:"scissors",2:"rock"}
hands = ("rock","paper","scissors")
player_history = []
machine_hand = hands[randint(0,2)]
game = True
while game == True:
    player_hand = input("Rock, paper, or scissors? (input lowercase): ")
    player_history.append(int(scores[player_hand]))
    rps(machine_hand, player_hand)
    machine_hand = choice[round(sum(player_history)/len(player_history))]
    repeat_game = input("Play again? (Y/N): ")
    if repeat_game == "Y" or repeat_game =="y":
        continue
    else:
        game = False
exit()