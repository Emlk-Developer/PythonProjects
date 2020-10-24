# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:35:58 2020

@author: owner
"""

from random import choice

lottery = ['A','B','C','D',1,2,3,4,5,]
my_ticket = ['B','C',4,2]
winningnumbers = []

class TheLotto:
    
    def __init__(self):
        self.draw = draw
    
        
    def thedraw(self):
        #retrieves 4 characters fro the lottery array and stores in winningnumbers
        for i in range(4):
            i +=1 
            getnumber = choice(lottery)
            winningnumbers.append(getnumber)
        print(f"The winning numbers are {winningnumbers}")
            


active = True
counter = 1
while active:
        #call the class
        haveIwon = TheLotto
        #create an instance
        haveIwon.thedraw('not yet')
        counter +=1
        if my_ticket != winningnumbers:
            #delete the array
            winningnumbers.clear()
            print(f"fail {counter}")
            
        else:
            print(f"I won {winningnumbers}")  
            active = False
    