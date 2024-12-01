# Part1
import re

cumulative_sum = 0
with open("day3_input.txt") as f:
    text = f.readlines()

def isValid(curr_row, curr_ind, last_index):
    next_index = last_index if last_index<141 else last_index-1
    prev_ind = curr_ind if curr_ind==0 else curr_ind-1
    if curr_row>0:
        characters = text[curr_row-1][prev_ind:next_index]
        if re.search(r'[^\w.]', characters):
            return False
    if curr_row<len(text)-1:    
        characters = text[curr_row+1][prev_ind:next_index]
        if re.search(r'[^\w.]', characters):
            return False 
    if re.search(r'[^\w.]', text[curr_row][prev_ind]):
        return False
    if re.search(r'[^\w.]', text[curr_row][next_index-1]):
        return False
    return True

for index, line in enumerate(text):
    line_length = len(line)
    digit_matches = re.finditer(r'\d+', line)
    result = [(match.group(), match.start(), match.end()+1) for match in digit_matches]
    for r in result:
        if not isValid(index, r[1], r[-1]):
            cumulative_sum+=int(r[0])


print(cumulative_sum)


# part2

from operator import mul
gear_regex = r'\*'
gears = dict()
for i, line in enumerate(text):
    for m in re.finditer(gear_regex, line):
        gears[(i, m.start())] = []

number_regex = r'\d+'
for i, line in enumerate(text):
    for m in re.finditer(number_regex, line):
        for r in range(i-1, i+2):
            for c in range(m.start()-1, m.end()+1):
                if (r, c) in gears:
                    gears[(r, c)].append(int(m.group()))

gear_ratio_sum = 0
for nums in gears.values():
    if len(nums) == 2:
        gear_ratio_sum += mul(*nums)

print(gear_ratio_sum)
