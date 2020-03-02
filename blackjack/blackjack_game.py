#!/usr/bin/env python3
# Blackjack Game]
from time import sleep
from blackjack_cards import *
from blackjack_hand import *
class Game:
    def __init__(self):
        pass
    def play(self):
        print("""
                                                                                   
88          88                       88        88                       88""")
        sleep(0.1)
        print(
"""88          88                       88        ""                       88""")         
        sleep(0.1)
        print(
"""88          88                       88                                 88""")
        sleep(0.1)
        print(
"""88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8""")
        sleep(0.1)
        print(
"""88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8" """)
        sleep(0.1)
        print(
"""88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      """)
        sleep(0.1)
        print(
"""88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   """)
        sleep(0.1)
        print(
"""8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  """)
        sleep(0.1)
        print(
"""                                              ,88                                  """)
        sleep(0.1)
        print(
"""                                            888P"                                  """)
        sleep(0.1)
        print("""
========A Simple Blackjack Game, Written In Python================================""")
        sleep(0.1)
        print(
"""=============================================Welcome To The Table=================""")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print("Good evening, I will be your dealer for this evening...\n")
        sleep(3)
        playing = True
        while playing:
            deck_choice = True
            while deck_choice:
                decks = input("\nHow many decks should we play with today?: ")
                if decks.isnumeric():
                    decks = int(decks)
                    deck_choice = False
                    break
                else:
                    print("\nI'm sorry, I could swear that wasn't a number...")
                    sleep(1)
                    print("...So... ", end = " ")
                    continue
            self.deck = deck(decks)
            self.deck.shuffle()
            hands = True
            while hands:
                self.player_hand = hand()
                self.dealer_hand = hand(dealer=True)
                for i in range(2):
                    self.player_hand.add_card(self.deck.deal())
                    self.dealer_hand.add_card(self.deck.deal())
                print("\nAre you ready?\n")
                sleep(2)
                print("Then I'll deal...\n")
                sleep(2)
                print("Your hand is:")
                self.player_hand.display()
                print()
                print("My hand is:")
                self.dealer_hand.display()
                game_over = False
                while not game_over:
                    player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                    if player_has_blackjack or dealer_has_blackjack:
                        game_over = True
                        self.show_blackjack_results(
                            player_has_blackjack, dealer_has_blackjack)
                        continue
                    choice = input("\nWould you like to [Hit / Stick]?: ").lower()
                    while choice not in ["h", "s", "hit", "stick"]:
                        choice = input("\nI'm sorry that didn't make sense...\n You should try 'H', 'S', 'Hit', or 'Stick': ").lower()
                    if choice in ['hit', 'h']:
                        self.player_hand.add_card(self.deck.deal())
                        self.player_hand.display()
                        if self.player_is_over():
                            print("\nLooks like you've gone bust there...\n...tough luck.")
                            game_over = True
                    else:
                        player_hand_value = self.player_hand.get_value()
                        dealer_hand_value = self.dealer_hand.get_value()

                        print("\nSo at the end of that hand;")
                        print("\nYour score was", player_hand_value, end = " ")
                        print(", and mine was", dealer_hand_value)

                        if player_hand_value > dealer_hand_value:
                            print("\nLooks like you won.")
                        elif player_hand_value == dealer_hand_value:
                            print("\nWell look at that...\n...it's a tie.")
                        else:
                            print("\nHa!\nI've won...")
                        game_over = True
                again = input("\nAnother hand? [Y/N] ")
                while again.lower() not in ["y", "n"]:
                    again = input("\nI didn't catch that...\nDid you say Y or N? ")
                if again.lower() == "n":
                    print("\n")
                    hands = False
                else:
                    game_over = False
            deck_renew = input("Should we start a new game? [Y/N] ")
            while deck_renew.lower() not in ["y", "n"]:
                deck_renew = input("I didn't catch that...\nDid you say Y or N? ")
            if deck_renew.lower() == "n":
                print("\n...It's been a pleasure.\n")
                sleep(3)
                playing = False
                break
            else:
                continue
    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        return player, dealer
    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win!")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")
    def player_is_over(self):
        return self.player_hand.get_value() > 21