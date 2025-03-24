import phantom_poker_decks as decks
import random
import phantom_poker_multipliers as multipliers

#General variables
deck = decks.standard_deck
hand_size = 8
hand = []
selected_hand = []
selected_cards = []
played_hand = []
value = 0
multiplier = 1
ranks = [
    "1","2","3","4","5","6","7","8","9","10","A","K","Q","J"
]

A = 0
K = 0
Q = 0
J = 0

def draw_hand():
    for i in range (len(hand),hand_size):
        card = random.choice(list(deck))
        if card in hand:
            hand.remove(card)
        hand.append(card)

def select_cards():
    selected_cards = input(f"Please pick 5 of these cards: {hand} \n").replace(" ","").upper().split(",")
    if selected_cards:
        print(selected_cards)
    if len(selected_cards) > 5:
        print("You can't pick more than 5 cards!")
        select_cards()
    for card in selected_cards:
        if card not in hand:
            print(f"You do not have {card}!")
            selected_hand.clear()
            select_cards()
        elif card in selected_hand:
            print("Can't select the same card twice!")
        else:
            selected_hand.append(card)

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

def count_suits(played_hand):
    H = 0
    D = 0
    S = 0
    C = 0
    for card in played_hand:
        if card[0] == "H":
            H += 1
        if card[0] == "D":
            D += 1
        if card[0] == "S":
            S += 1
        if card[0] == "C":
            C += 1
    print(H,D,S,C)

def count_ranks(played_hand):
    rank_counts = {
        "A": 0, "K": 0, "Q": 0, "J": 0,
        "10": 0, "9": 0, "8": 0, "7": 0, "6": 0,
        "5": 0, "4": 0, "3": 0, "2": 0
    }

    for card in played_hand:
        rank = card[1:]
        if rank in rank_counts:
            rank_counts[rank] += 1
    print(rank_counts)
    return rank_counts

        

while True:
    draw_hand()
    select_cards()
    print(selected_hand)
    choice = input("Do you want to play or discard this deck? p/d \n").lower()
    if choice == "p":
        play()
    elif choice == "d":
        print(selected_hand)
        discard()
        print(selected_hand)
    count_suits(played_hand)
    count_ranks(played_hand)
    print(count_value())