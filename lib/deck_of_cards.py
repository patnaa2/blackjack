## Author: Anshuman Patnaik

from enum import Enum
from random import shuffle

VALID_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                'J', 'Q', 'K', 'A', 'Jo']

class Suit(Enum):
    hearts = 1
    spades = 2
    diamonds = 3
    clubs = 4


class Card(object):
    def __init__(self, value, suit, check=True):
        if check:
            if value not in VALID_VALUES:
                raise Exception("Invalid Value specified for Card")

            if type(suit) != Suit:
                raise Exception("Suit must be of type Suit")

        self.value = value
        self.suit = suit

    def __str__(self):
        return "%s of %s" %(self.value, Suit(self.suit).name)

    def __repr__(self):
        return "%s, %s" %(self.value, self.suit)


class Deck(object):
    def __init__(self, deck_size=1, min_deck_size=0,
                 cycle=True, jokers=False):
        if min_deck_size > deck_size:
            raise Exception("Minimum deck size must be larger than deck size")
        self.deck_size = deck_size
        self.min_deck_size = min_deck_size
        self.cards = []
        self.cycle = cycle
        self.jokers = jokers

    @property
    def cards_in_one_deck(self):
        if self.jokers:
            return (len(VALID_VALUES) * len(Suit)) + 2

        return len(VALID_VALUES) * len(Suit)

    def refill_deck(self):
        cards_to_add = []
        for _ in (self.deck_size - (len(self.cards)/self.cards_in_one_deck + 1):
            cards_to_add.append([Card(v, s, check=False)
                for s in Suit for v in VALID_VALUES])
        shuffle(cards_to_add)
        self.cards.extend(cards_to_add)

    @property
    def remaining_cards(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def deal_next_card(self):
        self.cards.pop()
