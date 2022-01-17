# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:29:16 2020

@author: owner
"""

import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline


#Make An API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url, headers=headers)
print(f"Status Code:{r.status_code}")

#API requests are returned in json format
#use json() method to convert to a Python Dictionary
#response dict is a Dictionary, not varible
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#headings of the dictionary
#keys() == are the headings of the files
print(response_dict.keys())


#Explore information about the repositories
rep_dicts = response_dict['items']
print(f"Repositories returned: {len(rep_dicts)}")

#examine the first repository
first_repo = rep_dicts[0]
len_repo = len(rep_dicts)
#print(f"\nKeys: {len(first_repo)}")
#for key in sorted(first_repo.keys()):
   # print(key)

#print(second_repo.keys())

"""
print("Selected information from repository")
for eachrep in rep_dicts:
    print(f"Name: {first_repo['name']}")
    print(f"Owner: {first_repo['owner']['login']}")
    print(f"Stars: {first_repo['stargazers_count']}")
    print(f"Repository: {first_repo['html_url']}")
    print(f"Created: {first_repo['created_at']}")
    print(f"Updated: {first_repo['updated_at']}")
    print(f"Description: {first_repo['description']}")
    print("\n\n....")
"""

starcount, reponames = [],[]
for eachrep in rep_dicts:
        names = eachrep['name']
        reponames.append(names)
        stars = eachrep['stargazers_count']
        starcount.append(stars)

    
#visualise the results
data = [{
        'type':'bar',
        'x':reponames,
        'y':starcount,
        'marker':{
                'color':'rgb(50,205,50)', #limegreen
                'line':{'width':1.5,'color':'rgb(255,0,0)'}
                },
        'opacity':0.6,
        
        }]

x_axis_config = {'title': 'Name'}
y_axis_config = {'title': 'Stargazer Count'}

my_layout = Layout(title='Most Starred Python Proejcts',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout}, filename='starcount.html')





