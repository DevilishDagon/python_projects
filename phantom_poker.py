import phantom_poker_decks as decks
import random
import phantom_poker_multipliers as multipliers

#General variables
played = False
deck = decks.standard_deck
hand_size = 8
hand = []
selected_hand = []
selected_cards = []
played_hand = []
value = 0
multiplier = 1
rank_counts = {
        "A": 0, "K": 0, "Q": 0, "J": 0,
        "10": 0, "9": 0, "8": 0, "7": 0, "6": 0,
        "5": 0, "4": 0, "3": 0, "2": 0
    }
suit_counts = {
    "H" : 0, "D" : 0, "S" : 0, "C" : 0
}

A = 0
K = 0
Q = 0
J = 0

def draw_hand():
    while len(hand) < hand_size:
        card = random.choice(list(deck))
        if card not in hand:
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
    selected_hand.clear()

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
    suit_counts = {
        "H":0,"D":0,"S":0,"C":0
    }

    for card in played_hand:
        suit = card[0]
        print(suit)
        suit_counts[suit] += 1
        print(suit_counts)

    return suit_counts

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

def check_flush(suit_counts):
    multiplier = 1
    for suit in suit_counts:
        if suit == 5:
            multiplier = multipliers.flush
    
    return multiplier

while not played:
    draw_hand()
    hand = ["HK", "HQ", "HJ", "HA", "H1"]
    select_cards()
    print(selected_hand)
    choice = input("Do you want to play or discard this deck? p/d \n").lower()
    if choice == "p":
        play()
        played = True
    elif choice == "d":
        print(selected_hand)
        discard()
        print(selected_hand)
count_suits(played_hand)
count_ranks(played_hand)
print(count_value())
multiplier = check_flush(suit_counts)
value = count_value()
final_value = value*multiplier
print(final_value)