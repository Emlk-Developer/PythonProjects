# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:09:48 2020

@author: owner
Black Jack

Variables:
    Deck array
    Player Hand array
    Dealer Hand array
    
Aces:
    are 1 or 11, in initial deal aces are 11
    
Functions:
    count play hand
    check for blackjack
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


Deck = ['A',2,3,4,5,6,7,8,9,10,10,10,10,
        'A',2,3,4,5,6,7,8,9,10,10,10,10,
        'A',2,3,4,5,6,7,8,9,10,10,10,10,
        'A',2,3,4,5,6,7,8,9,10,10,10,10,]
Player = []
Dealer = []
BlackJackHand = [[10,'A'],['A',10]]


random.shuffle(Deck)

def CheckBlackJack():
    #Check for BlackJack
    if Player in BlackJackHand:
        print(f"{Player} BlackJack! you win!")
        NewGame()
        
        
    
def CalculatePlayerHand():
    #Add together the number of players hands
    i = 0
    calculate = 0
    global PlayerTotal
    while i < len(Player):
        currentcard = Player[i]
        if currentcard == 'A':
            currentcard = 11
        i +=1
        calculate += currentcard
    PlayerTotal = calculate
    print(f"the player has {Player}")
    if PlayerTotal == 21:
        print("Blackjack")
        NewGame()
    elif PlayerTotal > 21:
        print("Bust")
        NewGame()
    else:
        print(f"{PlayerTotal}")
    
        
def CalculateDealerHand():
    #Add together the number of players hands
    i = 0
    calculate = 0
    global DealerTotal
    while i < len(Dealer):
        currentcard = Dealer[i]
        if currentcard == 'A':
            currentcard = 11
        i +=1
        calculate += currentcard
    DealerTotal = calculate
    print(f"dealer has {Dealer} total is {calculate}")
    if DealerTotal == 21:
        print("Blackjack! Player loses")
        NewGame()
    elif DealerTotal > 21:
        print("Bust! Player wins")
        NewGame()
    else:
        print(f"{DealerTotal}")
        
        
def CalculateDealerHandtoWin():
    CalculateDealerHand()
    if DealerTotal > PlayerTotal:
        print("Dealer has better hand, you lose")
        NewGame()
    elif DealerTotal >= 18 and DealerTotal < PlayerTotal:
        print("Player has a better hand, dealer loses")
        NewGame()
    elif DealerTotal >= 18 and DealerTotal == PlayerTotal:
        print("It's a draw")
        NewGame()
    
        
    
def Deal():
    Player.append(Deck.pop())
    Player.append(Deck.pop())
    CheckBlackJack()
    CalculatePlayerHand()
    Dealer.append(Deck.pop())
    CalculateDealerHand()
    
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
    
    
def Hit():
    Player.append(Deck.pop())
    CalculatePlayerHand()
   
    
def Stand():
    while DealerTotal < 18:
        Dealer.append(Deck.pop())
        CalculateDealerHandtoWin()
    
    
def NewGame():
    newGame = input("would you like to play again? Y or N ")
    if newGame == "Y":
        Player.clear()
        Dealer.clear()
        DealerTotal = 0
        PlayerTotal = 0
        Deal()    
    
    
#Start game, dealer has one card player has two.
Deal()


