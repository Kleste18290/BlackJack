import random

    # "Key":value
deck = {"Ace of hearts":0, "Two of hearts":2, "Three of hearts":3,
                      "Four of hearts":4, "Five of hearts":5, "Six of heart":6,
                      "Seven of hearts":7, "Eight of hearts":8, "Nine of hearts":9,
                      "Ten of hearts":10, "Jack of hearts":10, "King of hearts":10, 
                      "Queen of hearts":10 }

hand = 19


if hand > 21:
    deck["Ace of hearts"] == 1
else:
    deck["Ace of hearts"] == 11

def players_hand(hand):
    # This will hold the players cards and clear at 
    # the start of every round.

    if sum(hand) > 21:
        print("You have more than a value of 21 in your hand, you have lost the game!")
        hand.clear
    pass

def add_card():
    # This will add a card to the players hand on request.
    print("Do you wish to add another card?")

    print(random.randrange(deck))

add_card()


def player_wins():
    # A counter that will keep track of the players wins.
    pass

print(deck["Ace of hearts"])


