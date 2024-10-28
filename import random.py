import random

    # "Key":value
def deck_of_cards(hand):

    deck = {
        "Ace of hearts":11, 
        "Two of hearts":2, 
        "Three of hearts":3,
        "Four of hearts":4, 
        "Five of hearts":5, 
        "Six of heart":6,
        "Seven of hearts":7, 
        "Eight of hearts":8, 
        "Nine of hearts":9,
        "Ten of hearts":10, 
        "Jack of hearts":10, 
        "King of hearts":10, 
        "Queen of hearts":10 
        }
    
    res = key, val = random.choice(list(deck_of_cards.items()))
        
    if hand > 21:
        deck["Ace of hearts"] = 1       
    
    print(str(res))
    
def player_hand(deck):
    # Players hand that accumulates card values.
    # These will be printed to the screen. 
    


    total_hand = "Equation for card accumulation here."
    return total_hand

def game_conditions(total_hand)
    if total_hand > 21
        print("Your hand holds a greater value than 21, you have lost the game!")


