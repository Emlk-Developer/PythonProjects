# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:09:48 2020

@author: owner
Black Jack

Variables:
    Deck array
    Player Hand array
    Dealer Hand array
    
Functions:
    count play hand
    count dealer hand
    Hit a card
    Stand and dealer deals cards
    
Results:
    Did you bust
    did you stick under 21
    was your card count better than dealers
    did dealer bust
"""
#from random import randint
import random


Deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10]
Player = []
Dealer = []



random.shuffle(Deck)


def CalculatePlayerHand(): 
    #Add together the number of players hands
    i = 0
    calculate = 0
    global PlayerTotal
    while i < len(Player):
        currentcard = Player[i]
        i +=1
        calculate += currentcard
    PlayerTotal = calculate
    print(f"the player has {Player}")
    if PlayerTotal == 21:
        print("Blackjack")
    elif PlayerTotal > 21:
        print("Bust")
    else:
        print(f"{PlayerTotal}")
    
        
def CalculateDealerHand(): 
    #Add together the number of players hands
    i = 0
    calculate = 0
    global DealerTotal
    while i < len(Dealer):
        currentcard = Dealer[i]
        i +=1
        calculate += currentcard
    DealerTotal = calculate
    print(f"dealer has {Dealer} total is {calculate}")
    if DealerTotal == 21:
        print("Blackjack! Player loses")
    elif DealerTotal > 21:
        print("Bust! Player wins")
    else:
        print(f"{DealerTotal}")
        
        
    
def Deal():
    Player.append(Deck.pop())
    Player.append(Deck.pop())
    CalculatePlayerHand()
    Dealer.append(Deck.pop())
    CalculateDealerHand()
    
def Hit():
    Player.append(Deck.pop())
    CalculatePlayerHand()

    
    
    
def Stand():
    while DealerTotal < 18:
        Dealer.append(Deck.pop())
        CalculateDealerHand()
    
    
    
#Start game, dealer has one card player has two.
Deal()

while PlayerTotal < 21 and DealerTotal < 18:
    try:
        HitorStand = input("Hit or Stand? (type Quit to end)")
    except ValueError:
        print("please either type in Hit or type Stand")
        
    if HitorStand == "Hit":
        Hit()
    elif HitorStand == "Stand":
        Stand()
    elif HitorStand == "Quit":
        break

