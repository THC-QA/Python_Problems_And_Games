#!/usr/bin/env python3.8
# Blackjack_Cards
import random
class card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return " of ".join((self.value, self.suit))
class deck:
    def __init__(self, decks):
        self.cards = [card(s,v) for s in ["♠", "♥", "♣", "♦"] for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]*decks
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

