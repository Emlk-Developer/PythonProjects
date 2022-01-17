# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:24:00 2020

@author: owner
"""

#get request

import json
import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
#because doing an API request from github, need to declare which version
#we want to work with.
headers={'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
loadruby = r.json()

print(f"status code: {r.status_code}")

#prints headings from the json file
print(loadruby.keys())

RubyItemHeading = loadruby['items']

print(len(RubyItemHeading))


#return first line of repository to get the headings within items
FirstRepHeadings = RubyItemHeading[0]
HeadingKeys = FirstRepHeadings.keys()
#print(HeadingKeys)


#Return the name within the FirstRepHeading
FirstName = FirstRepHeadings['name']
#print(f"the name is : {FirstName}")


Language = FirstRepHeadings['language']
print(Language)

#return all the names and star count in the Repository
TheNames = []
StarCount = []
for AllNames in RubyItemHeading:
    thename = AllNames['name']
    TheNames.append(thename)
    stars = AllNames['stargazers_count']
    StarCount.append(stars)
    
    
print(TheNames,StarCount)

#visualise the results
data = [{
        'type':'bar',
        'x':TheNames,
        'y':StarCount,
        'marker':{
                'color':'rgb(50,205,50)', #limegreen
                'line':{'width':1.5,'color':'rgb(255,0,0)'}
                },
        'opacity':0.6,
        
        }]

x_axis_config = {'title': 'Name'}
y_axis_config = {'title': 'Stargazer Count'}

my_layout = Layout(title=f"Most Starred {Language} Projects",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout}, filename='starcountRuby.html')





    
    




"""
for RubyItems in RubyItemHeading[:3]:
    print(f"item is: {RubyItems}")
    print(f"\n\n")
    
"""