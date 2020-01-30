# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:37:32 2020
@author: user
"""
#<span class="sportsbook-odds american default-color">+1800</span>

import requests
from bs4 import BeautifulSoup
url = "https://sportsbook.draftkings.com/leagues/basketball/103?category=game-lines&subcategory=game"
page = requests.get(url)
#print(page.status_code)  #200 returned means okay
#print(page.headers)   #returns page headers, shows url where at

soup = BeautifulSoup(page.content, 'html.parser')
# <section class=sportsbook-table> I think this has todays matches??
table = soup.find('section', class_='sportsbook-table')

trs = table.find_all('div', class_='sportsbook-table__column-row')

for tr in trs:
    tds = soup.find_all('span', class_='sportsbook-odds american default-color') #tds is odds
    team_names = soup.find_all('span', class_="event-cell__name")
    visitor_name = team_names[0].find('span').contents[0].strip()
    home_name = team_names[1].find('span').contents[0].strip()
    print(visitor_name)
    print(home_name)

#links = soup.find_all('a')  finds all a tabs which are links and puts them to list


#print(links) prints the variable link
#print(divs)
#print('\n') prints a line return at end.


#eventcellname = soup.find('div', class_= 'event-cell__name')


