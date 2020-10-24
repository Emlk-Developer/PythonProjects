# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 08:06:36 2020

@author: owner

testing the clas AnonymousSurvey
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    #tests to test the class
    
    def setUp(self):
        #setup will be run bfore the test methods
        #create a survey and set of responses to be used in the test methods
        question = "name three languages"
        self.langsurvey = AnonymousSurvey(question)
        self.responses = ['English','French','Spanish'] 
        

    def test_storesingleresponse(self):
        #test that a single response is stored inthe list
        self.langsurvey.storeresponse(self.responses[0])
        self.assertIn(self.responses[0],self.langsurvey.response)
        
    def test_storethreeresponses(self):
        #testing multiple responses are stored in the list response
        #add the responses to the storeresponse
        for response in self.responses:
            self.langsurvey.storeresponse(response)
       
        #check that each response is in the new list storeresponse
        for response in self.responses:
            self.assertIn(response,self.langsurvey.response)
        
    
    
if __name__ == '__main__':
    unittest.main()
    

