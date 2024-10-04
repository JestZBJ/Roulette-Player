# create a Computer object that can have it's own hand and go through a series of ifs to decide what to do
# deal - deals one card
# deal_blackjack_hand - deals a hand for blackjack alternating from User to Comp

import random

def new_standard_deck():
    deck = []
    suits = ["C", "H", "S", "D"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for i in range(len(suits)):
        for j in range(len(values)):
            card = values[j] + suits[i]
            deck.append(card)
    
    return deck

    '''for i in range(4):
        for j in range(13):
            if len(deck) <= 12:
                c = str(j + 1) + "C"
                deck.append(c)
            elif len(deck) <= 25 and len(deck) > 12:
                h = str(j + 1) + "H"
                deck.append(h)
            elif len(deck) <= 38 and len(deck) > 25:
                s = str(j + 1) + "S"
                deck.append(s)
            elif len(deck) <= 52 and len(deck) > 38:
                d = str(j + 1) + "D"
                deck.append(d)'''

def new_uno_deck():
    deck = []
    suits = ["R", "G", "B", "Y"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "SKIP", "REV."]

    for i in range(len(suits)):
        card = suits[i] + "0"
        deck.append(card)
        for j in range(len(values)):
            for x in range(2):
                card = suits[i] + values[j]
                deck.append(card)
    
    for a in range(4):
        deck.append("WILD")
    
    for b in range(4):
        deck.append("+4")

    return deck

def new_custom_deck():
    deck = []

    # ask for suit and value input

    '''for i in range(len(suits)):
        for j in range(len(values)):
            card = suits[i] + values[j]
            deck.append(card)'''

def play_blackjack():
    deck = new_standard_deck()
    random.shuffle(deck)

    '''
    alternate dealing to player and computer
        each participant has their own list as hand
        read the first item in the list and add it to next participant's hand
        delete it from deck then repeat
    computer reveals first card
    read input from user
        hit:  deal another
        stand: go to computer
    computer goes by if:then to detirmine hit or pass
        <=16: hit
        >=17: stand
    after each hit check to see if bust

    Display
        Dealer's hole card: __

        Your hand: __
        Hit or Stand?
        Hit

        Dealt: __
        Your hand: __
        Hit or Stand?
        Stand

        Dealer's Turn -
        Dealer's hand: __
        Hit

        Dealt: __
        Dealer's hand: __
        Stand

        Results - (You / Dealer) Win(s)
    '''



un = new_standard_deck()
print(un)