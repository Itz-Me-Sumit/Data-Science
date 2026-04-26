import random
from dataclasses import dataclass

# Card Model (single card)
@dataclass(frozen=True)
class Card:
    value: str
    suit: str

    def __str__(self):
        return f"{self.value} of {self.suit}"

# Deck Class
class Deck:

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    VALUES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    def __init__(self):
        self._cards = self._create_deck()
        self.shuffle()

    def _create_deck(self):
        deck = []

        for suit in self.SUITS:          # Spades, Hearts, ...
            for value in self.VALUES:    # ace, 2, 3 ... king
                deck.append(Card(value, suit))

        return deck

    def shuffle(self):
        random.shuffle(self._cards)

    def deal_one(self):
        if self.is_empty():
            raise ValueError("No cards left in the deck")
        return self._cards.pop()

    def deal_many(self, count):
        if count > len(self._cards):
            raise ValueError("Not enough cards to deal")
        return [self.deal_one() for _ in range(count)]

    def is_empty(self):
        return len(self._cards) == 0

    def remaining_cards(self):
        return len(self._cards)


# Player Class 
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return [str(card) for card in self.hand]


# Example Usage
if __name__ == "__main__":
    deck = Deck()

    player1 = Player("Sumit")
    player2 = Player("Rahul")

    # each gets 5 cards
    player1.receive_cards(deck.deal_many(5))
    player2.receive_cards(deck.deal_many(5))

    print("Player 1 Hand:")
    print(player1.show_hand())

    print("\nPlayer 2 Hand:")
    print(player2.show_hand())

    print("\nRemaining cards:", deck.remaining_cards())