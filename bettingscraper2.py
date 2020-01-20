# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:04:38 2020

@author: James
"""

"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import datetime 



url = "https://www.bettingpros.com/nba/odds/moneyline/"
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
tbody = soup.find('tbody', class_='odds-table__tbody tbody')

trs = tbody.find_all('tr')
#tr = trs[0]
sources = ['Betting Pros', 'Fanduel', 'DraftKings', 'BetMGM']

with open('betting_lines.txt', 'a') as f:
    
    now = datetime.datetime.now()
    now_string = now.strftime('# %x %X')
    
    f.write(', '.join([now_string, ''] + sources) + '\n')
    
    for tr in trs:
        
        tds = tr.find_all('td', class_='odds-table__td book-cell')
        #td = tds[0]
        
        team_names = tr.find_all('div', class_='team-name')
        visitor_name = team_names[0].find('div').contents[0].strip()
        home_name = team_names[1].find('div').contents[0].strip()
        
        visitor_max = (float('-inf'), '')   # Visitor max is a tuple (value, src)
        home_max = (float('-inf'), '')      # Visitor max is a tuple (value, src)
        
        visitor_vals = []
        home_vals = []

        for td, src in zip(tds, sources):
     
            
            try:
                visitor = td.find('div', class_='line-container visitor')or \
                    td.find('div', class_='line-container visitor best tooltip')
                visitor_div = visitor.find('div', class_='line')
                visitor_val = int(visitor_div.contents[0].strip())
                visitor_vals.append(str(visitor_val))
                
                home = td.find('div', class_='line-container home') or \
                    td.find('div', class_='line-container home best tooltip')
                home_div = home.find('div', class_='line')
                home_val = int(home_div.contents[0].strip())
                home_vals.append(str(home_val))
    
                visitor_max = max((visitor_val, src), visitor_max)
                home_max = max((home_val, src), home_max)
                                
                print(src, ':', home_name, home_val, ',', visitor_name, visitor_val)
                
                
            except AttributeError:
                print('!', src, 'couldn\'t find home or visitor value')
                
        f.write(', '.join(['visitor', visitor_name] + visitor_vals) + '\n')
        f.write(', '.join(['home', home_name] + home_vals) + '\n')
        f.write('end game\n')
        
        if visitor_max[0] + home_max[0] > 0:
            print('   PROFITABLE SITUATION!  Bet the BEST LINES!!')
            print('     BEST LINE', visitor_max[1],':', visitor_name, ',', visitor_max[0])
            print('     BEST LINE', home_max[1],':', home_name, ',', home_max[0])
         #Just trying to add whitespace 
        print('')
        
        
        