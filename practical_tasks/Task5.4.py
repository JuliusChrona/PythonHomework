import random
from collections import namedtuple

Cards = namedtuple('card', ["suit", "value"])
card_suit = ("Hearts", "Diamonds", "Spades", "Clubs")
card_value = ('6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
CARDS_DECK = [Cards(suit=suit, value=value)
              for suit in card_suit
              for value in card_value
              ]


class Card():
    def __new__(self, suit, value):
        if (suit, value) not in CARDS_DECK:
            print("not correct card name, use card suit:",
                  card_suit, 'and card value:', card_value)
            return None
        else:
            return super().__new__(self)

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        print(f'Card: {suit} {value}')


class Deck():
    def __init__(self):
        self.copy_deck = CARDS_DECK[:]

    def shuffle(self):
        random.shuffle(self.copy_deck)

    def get_card(self):
        return self.copy_deck.pop() if self.copy_deck else 'Deck is empty'

    def get_remaining_amount_cards(self):
        return len(self.copy_deck)


if __name__ == '__main__':
    in_hand = []
    player = Deck()
    player.shuffle()
    for _ in range(6):
        in_hand.append(player.get_card())
    in_hand = [(suit, value) for suit, value in in_hand]
    print("In your hand six cards: ", end='')
    for card in in_hand:
        print(card[0], card[1], end=' ')
    print()
    print(player.get_remaining_amount_cards())
