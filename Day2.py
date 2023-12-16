import re

possible_games = 0
with open("day2_input.txt") as f:
    text = f.readlines()

allowed_limits = {
    "blue": 14,
    "red": 12,
    "green": 13
}

colour_count_splitup = []
for i, line in enumerate(text, 1):
    colour_count_splitup = re.findall(r'\b(\d+)\s+(blue|green|red)\b', line)
    impossible = False
    for eachSplit in colour_count_splitup:
        if int(eachSplit[0])>allowed_limits[eachSplit[-1]]:
            impossible = True
            break 
    if not impossible: possible_games+=i

print(possible_games)
    
# Part2

import re

cumulative_total = 0
with open("day2_input.txt") as f:
    text = f.readlines()

colour_count_splitup = []
for i, line in enumerate(text, 1):
    colour_count_splitup = re.findall(r'\b(\d+)\s+(blue|green|red)\b', line)

    max_colours = {
    "blue": 1,
    "red": 1,
    "green": 1
}
    for eachSplit in colour_count_splitup:
        max_colours[eachSplit[-1]] = max(max_colours[eachSplit[-1]], int(eachSplit[0]))

    total =max_colours["blue"] * max_colours["green"] * max_colours["red"]        
    cumulative_total+=total

print(cumulative_total)
    
