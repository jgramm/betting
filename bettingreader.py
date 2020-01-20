# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:19:06 2020

@author: James
"""


list_of_odds_at_specific_time = []

with open('betting_lines.txt', 'r') as f:
    
    data = {}
    
    for line in f:

        # split the line into separate values delimited by ', '
        vals = line.strip().split(', ')
        
        # Indicates we recorded data at a new time
        if line.startswith('#'):
            # append accumulated data to this list with everything in it
            list_of_odds_at_specific_time.append(data)
            print('old data', data)
            print('new stuff')
            
            # create a new dictionary of data
            data = {}
            # store the time (ignoring the '# ' at the start)
            data['time'] = vals[0][2:]
            # sources start at column 2
            sources = vals[2:]
            data['sources'] = sources
            # we're going to be looking at a new game
            game = {}   
        
        # Indicates that the game that we're looking at is done
        elif line.startswith('end game'):
            # the key for this game will be the name of the home team
            # make sure to do game.copy because game is immutable
            data[game['home'][0]] = game.copy()
            
        # Otherwise
        else:
            # store the team type (home/away), the team name, and the odds
            team_type = vals[0]
            team_name = vals[1]
            odds = vals[2:]
            # store this data into the game dictionary
            game[team_type] = (team_name, odds)
            
    
    list_of_odds_at_specific_time.append(data)