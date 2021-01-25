'''
Card Class
Suit, Rank, Value
'''
from global_var import *

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.a = a

    def __str__(self):
        return self.rank + " of " + self.suit

    def get_a(self):
        print(type(a))