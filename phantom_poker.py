import phantom_poker_decks as decks
import random
import phantom_poker_multipliers as multipliers

deck = decks.standard_deck
hand_size = 8
hand = []
selected_hand = []
selected_cards = []
played_hand = []

def draw_hand():
    for i in range (len(hand),hand_size):
        card = random.choice(list(deck))
        if card in hand:
            draw_hand()
        hand.append(card)

def select_cards():
    selected_cards = input(f"Please pick 5 of these cards: {hand} \n")
    selected_cards = selected_cards.split(",")
    if len(selected_cards) > 5:
        print("You can't pick more than 5 cards!")
        select_cards()
    for card in selected_cards:
        if card not in hand:
            print(f"You do not have {card}!")
            select_cards()
        elif card not in selected_hand:
            selected_hand.append(card)
        else:
            print("Can't pick the same card twice!")
            select_cards()

def discard():
    for card in selected_hand:
        deck.pop(card)
        hand.remove(card)
        selected_hand.remove(card)

def play():
    for card in selected_hand:
        played_hand.append(card)
            
def count_value():
    value = 0
    for card in played_hand:
        value += (deck[card])
        deck.pop(card)
    return value

while True:
    draw_hand()
    select_cards()
    print(selected_hand)
    choice = input("Do you want to play or discard this deck? p/d \n").lower()
    if choice == "p":
        play()
    elif choice == "d":
        discard()
    print(count_value())