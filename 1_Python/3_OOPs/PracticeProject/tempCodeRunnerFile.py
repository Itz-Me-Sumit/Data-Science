import random

class Deck:
    
    Cards = {
        1: ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        2: ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        3: ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        4: ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    }

    def CardName(self, num):
        names = {
            1: "Spades",
            2: "Hearts",
            3: "Diamonds",
            4: "Clubs"
        }
        return names[num]

    def deal(self):
        if len(Deck.Cards) == 0:
            return "All Cards Dealt"

        # Random suit pick karo (existing keys se)
        suit = random.choice(list(Deck.Cards.keys()))

        # Random card pick karo
        card = random.choice(Deck.Cards[suit])

        # Remove card
        Deck.Cards[suit].remove(card)

        # Agar suit empty ho gaya to hata do
        if len(Deck.Cards[suit]) == 0:
            del Deck.Cards[suit]

        return f"{card} of {self.CardName(suit)}"

myCard = Deck()
for _ in range(52):
    print(myCard.deal())