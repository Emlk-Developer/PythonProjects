# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 07:35:15 2020

@author: owner

testing a class

"""

class AnonymousSurvey:
    
    def __init__(self,question):
        #store a question, store response in a list
        self.question = question
        self.response = []
        
        
    def showquestion(self):
        #show the question
        print(self.question)
        
        
    def storeresponse(self,newresponse):
        #store response
        self.response.append(newresponse)
        
        
    def showresponse(self):
        #show all the response in list
        for responses in self.response:
            print(responses)
        
        
        

