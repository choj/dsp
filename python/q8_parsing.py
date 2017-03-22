# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

# read in football.csv as pandas dataframe
fb_data = pd.read_csv("football.csv")

smallest_diff = abs(fb_data['Goals'] - fb_data['Goals Allowed'])

# get index of minimum smallest_diff value
smallest_index = smallest_diff[smallest_diff==min(smallest_diff)].index[0]

print(fb_data['Team'][smallest_index])