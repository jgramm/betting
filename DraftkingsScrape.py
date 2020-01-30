# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:37:32 2020
@author: user
"""
#<span class="sportsbook-odds american default-color">+1800</span>

import requests
from bs4 import BeautifulSoup

def parse_team_column(child):
    crs = child.find_all('div', 'sportsbook-table__column-row')
    team_names = []
    team_scores = []
    
    for cr in crs:
        
        try:
            team_info = cr.find('div', class_='event-cell__team-info')
            team_name = team_info.find('span', class_='event-cell__name')
            team_score = team_info.find('span', class_='event-cell__score')
            
            team_names.append(team_name.contents[0])
        except:
            team_names.append(None)

        # TODO: THIS FIX IS UGLY AND MAY BE NECESSARY FOR THE OTHER FUNCTIONS
        # FIGURE OUT HOW TO DO THIS BETTER
        try:
            team_scores.append(team_score.contents[0])
        except:
            team_scores.append(None)
    
    return team_names, team_scores


def parse_point_spread_column(child):
    crs = child.find_all('div', 'sportsbook-table__column-row')
    
    spreads = []
    odds = []
    for cr in crs:
        try:
            spread = cr.find('span', class_='sportsbook-outcome-cell__line').contents[0]
            odd = cr.find('span', class_='sportsbook-odds american default-color').contents[0]
            spreads.append(spread)
            odds.append(odd)
            
        except:
            spreads.append(None)
            odds.append(None)
    
    return spreads, odds


def parse_total_point_column(child):

    crs = child.find_all('div', 'sportsbook-table__column-row')
    
    over_unders = []
    over_under_vals = []
    odds = []

    for cr in crs:
        try:
            over_under = cr.find('span', class_='sportsbook-outcome-cell__label').contents[0]
            over_under_val = cr.find('span', class_='sportsbook-outcome-cell__line').contents[0]
            odd = cr.find('span', class_='sportsbook-odds american default-color').contents[0]
            
            over_unders.append(over_under)
            over_under_vals.append(over_under_val)
            odds.append(odd)
        
        except:
            over_unders.append(None)
            over_under_vals.append(None)
            odds.append(None)
    
    return over_unders, over_under_vals, odds


def parse_money_line_column(child):
    
    crs = child.find_all('div', 'sportsbook-table__column-row')
    money_lines = []

    for cr in crs:
        try:
            money_line = cr.find('span', class_='sportsbook-odds american default-color').contents[0]
            money_lines.append(money_line)
        except:
            money_lines.append(None)
        
    return money_lines
    

url = "https://sportsbook.draftkings.com/leagues/basketball/103?category=game-lines&subcategory=game"
page = requests.get(url)
#print(page.status_code)  #200 returned means okay
#print(page.headers)   #returns page headers, shows url where at

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('section', class_='sportsbook-table')
tb = table.find('div', class_='sportsbook-table__body')

team_vals = None
spread_vals = None
point_vals = None
money_vals = None


for i, child in enumerate(tb.children):
    
    if i == 0:
        team_vals = parse_team_column(child)
    elif i == 1:
        spread_vals = parse_point_spread_column(child)
    elif i == 2:
        point_vals = parse_total_point_column(child)
    elif i == 3:
        money_line_vals = parse_money_line_column(child)
    else:
        print('SHOULD NOT GET HERE!')
        
for team, team_odds, spread, spread_odds, o_u, o_u_val, o_u_odds, money_line in \
        zip(team_vals[0], team_vals[1], spread_vals[0], spread_vals[1], point_vals[0], point_vals[1], point_vals[2], money_line_vals):
    print(team, team_odds, spread, spread_odds, o_u, o_u_val, o_u_odds, money_line)
    


