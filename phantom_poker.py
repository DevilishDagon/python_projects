import phantom_poker_decks as decks
import random

deck = decks.standard_deck
hand_size = 5
hand = []

def draw_hand():
    for i in range (0,hand_size):
        card = random.choice(list(deck))
        hand.append(card)

def count_value():
    value = 0
    for card in hand:
        value += (deck[card])
    return value

def select_cards():
    selected_cards = input(f"Please pick 5 of these cards: {hand}")
    

draw_hand()
print(hand)
print(count_value())