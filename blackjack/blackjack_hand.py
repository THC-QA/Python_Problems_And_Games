#!/usr/bin/env python3
# Blackjack Hand
from blackjack_cards import *
class hand:
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        if self.dealer:
            self.dealerhit = False
    def add_card(self,card):
        self.cards.append(card)
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10
    def get_value(self):
        self.calculate_value()
        return self.value
    def display(self):
        if self.dealer:
            if self.dealerhit:
                for card in self.cards:
                    print(card)
            print("hidden")
            print(self.cards[1])
            self.dealerhit = True
        else:
            print("")
            for card in self.cards:
                print(card)
            print("Hand value: ", self.get_value())