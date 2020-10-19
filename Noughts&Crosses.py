# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:52:06 2020

@author: owner
display empty board
toss coin decide who goes first
first player goes
next player goes
alternate turns
check win
"""
import random

board = ["-1-","-2-","-3-",
         "-4-","-5-","-6-",
         "-7-","-8-","-9-",]

boardspaces = [0,1,2,3,4,5,6,7,8,]

headsORtails = ["heads", "tails"]
playersmoves = []
computersmoves = []


def displayBoard():
    print("-----------------------------")
    print(board[0]+ "|" + board[1]+ "|" + board[2]+ "|")
    print(board[3]+ "|" + board[4]+ "|" + board[5]+ "|")
    print(board[6]+ "|" + board[7]+ "|" + board[8]+ "|")
    print("----------------------------")



def tossCoin():
    playerschoice = input("enter heads or tails to go first : ")
    cointoss = random.choice(headsORtails)
    if playerschoice == cointoss:
        #player goes first
        print(f"{cointoss} it is, you go first")
        #global OorX 
        #OorX = input("do you want to be O or X ? : ")
    else:
        #computer goes first
        print(f" sorry it was {cointoss} computer goes first")
        computerPlay()
   
    
def playerPlay():
    
    location = int(input("where do you want to go? : "))    
    #checklocation is available
    playerchoice = location -1
    if playerchoice in boardspaces:
        boardspaces.remove(playerchoice)
        board[playerchoice] = "-O-" 
        playersmoves.append(playerchoice)
        playersmoves.sort()
        displayBoard()
        checkForWin()
        computerPlay()
    else:
        print(f"{location} has already been taken, choose another spot")
    
    
def checkForWin():
    #8 ways to win b = slice(2,6) x[b]
    waystowin = [[0,1,2],[3,4,5],[6,7,8],[1,4,7],[0,3,6],[2,5,8],[0,4,8],[2,4,6]]
    
    if playersmoves in waystowin:
        print("Player wins")
        playAgain()
        
    elif computersmoves in waystowin:
        print("Computer wins")
        playAgain()
    else:
        print("no winner yet")
        
        
def computerPlay():
    compchoice = random.choice(boardspaces)
    boardspaces.remove(compchoice)
    board[compchoice] = "-X-" 
    print(f"computer has picked spot {compchoice + 1}")
    computersmoves.append(compchoice)
    computersmoves.sort()
    displayBoard()
    checkForWin()
    playerPlay()
    
   
def playAgain():
    playagainYN = input("do you want to play again? Y or N")
    if playagainYN == "Y":
        board.clear()
        boardspaces.clear()
        playersmoves.clear()
        computersmoves.clear()
        board = ["-1-","-2-","-3-",
         "-4-","-5-","-6-",
         "-7-","-8-","-9-",]
        boardspaces = [0,1,2,3,4,5,6,7,8,]
        tossCoin()
        displayBoard()
        playerPlay()
    elif playagainYN == "N":
        SystemExit()
        
        

tossCoin()
displayBoard()
playerPlay()







