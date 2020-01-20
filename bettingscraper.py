# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import use
import requests
from bs4 import BeautifulSoup
url = 'https://www.bettingpros.com/nba/odds/moneyline/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
tbody = soup.find('tbody', class_='odds-table__tbody')

trs = tbody.find_all('tr')
sources = ['Betting Pros', 'FanDuel', 'DraftKings', 'BetMGM']

for tr in trs:
    
    tds = tr.find_all('td', class_='odds-table__td book-cell')
    
    team_names = tr.find_all('div', class_='team-name')
    visitor_name = team_names[0].find('div').contents[0].strip()
    home_name = team_names[1].find('div').contents[0].strip()
    
    for td, src in zip(tds, sources):
    
        try:
            visitor = td.find('div', class_='line-container visitor') or td.find('div', class_='line-container visitor best tooltip')
            visitor_div = visitor.find('div', class_='line')
            visitor_val = int(visitor_div.contents[0].strip())
            
            home = td.find('div', class_='line-container home') or td.find('div', class_='line-container home best tooltip')
            home_div = home.find('div', class_='line')
            home_val = int(home_div.contents[0].strip())
            
            print(src, ':', home_name, home_val, ',', visitor_name, visitor_val)
        
        except AttributeError:
            print('!', src, 'couldn\'t find home or visitor value')

    # Just trying to add whitespace here
    print('')
