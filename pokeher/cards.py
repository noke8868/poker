import functools
from handscore import *

@functools.total_ordering
class Suit(object):
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    __slots__ = ('suit')

    def __init__(self, suit):
        assert suit >= 0 and suit < len(self.SUITS)
        self.suit = suit

    def __repr__(self):
        return self.SUITS[self.suit]

    def __eq__(self, other):
        if isinstance(other, Suit):
            return self.suit == other.suit
        return NotImplemented

    def __lt__(self, other):
        return self.suit < other.suit

@functools.total_ordering
class Card(object):
    """Card value"""
    FACES = (None,None) + tuple(range(2, 11)) + ("J", "Q", "K", "A")
    __slots__ = ('value', 'suit')

    def __init__(self, value, suit):
        assert value > 1
        assert value < len(self.FACES)
        assert isinstance(suit, Suit)

        self.value = value
        self.suit = suit

    def is_pair(self, other):
        return self.value == other.value

    def is_suited(self, other):
        return self.suit == other.suit

    def score_value(self):
        if self.value < 10:
            return .01 * self.value
        else:
            return 0.1 * self.value

    def __repr__(self):
        return '{self.value}{self.suit.suit}'.format(self=self)

    def __str__(self):
        return '{value}-{suit}'.format(value=self.FACES[self.value], suit=str(self.suit))

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        return NotImplemented

    def __lt__(self, other):
        """Implements compare for Cards. Check value, then suit"""
        return ((self.value, self.suit) <
                (other.value, other.suit))

    @staticmethod
    def full_deck():
        """Returns a full deck of cards"""
        deck = []
        suits = (Suit(s) for s in range(0,4))
        for suit in suits:
            cards = (Card(c, suit) for c in range(2,15))
            for card in cards:
                deck.append(card)
        return deck

    @staticmethod
    def one_suit(suit_value):
        """Returns a single suit in a list"""
        suit = Suit(suit_value)
        return list(Card(c, suit) for c in range(2,15))

class Hand(object):
    """Player's hand of cards"""
    __slots__ = ('high', 'low')
    def __init__(self, card1, card2):
        if card1 > card2:
            self.high = card1
            self.low = card2
        else:
            self.high = card2
            self.low = card1

    def __repr__(self):
        return '{a}{b}'.format(a=repr(self.high), b=repr(self.low))

    def __str__(self):
        return '{a}, {b}'.format(a=self.high, b=self.low)

    def __eq__(self, other):
        if isinstance(other, Hand):
            return (self.high, self.low) == (other.high, other.low)
        return NotImplemented

    def is_pair(self):
        """Returns true if hand is a pair, false otherwise"""
        return self.high.value == self.low.value

    def is_suited(self):
        """Returns true if other and self are the same suit, false otherwise"""
        return self.high.suit == self.low.suit

    def card_gap(self):
        """Returns the gap between high & low"""
        return (self.high.value - self.low.value) - 1

    def is_connected(self):
        """Returns whether the hand is connected"""
        return self.card_gap() == 0

class Constants(object):
    CLUBS = Suit(0)
    DIAMONDS = Suit(1)
    HEARTS = Suit(2)
    SPADES = Suit(3)

    # Can use real numbers for everything else
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
