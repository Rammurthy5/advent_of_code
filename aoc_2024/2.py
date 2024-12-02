import os

with open("/Users/RSI03/aoc24/advent_of_code/aoc_2024/2.txt") as f:
    numbers = [l.split() for l in f.readlines()]

# part 1   
safe = 0
                 
for level in numbers:
    level = list(map(int, level))
    safe+=1

    if level[0]-level[1] in range(-3, 0):
        check_range = range(-3,0)
    elif level[0]-level[1] in range(1,4):
        check_range = range(1,4)
    else:
        safe-=1
        continue    
    for j in range(1, len(level)-1):
        res = level[j]-level[j+1]
        if res not in check_range:
            safe-=1
            break

print("part1 ",  safe)

# part 2
safe=0
def check_inc_dec(arr):
    inc_or_dec = (arr==sorted(arr) or arr==sorted(arr, reverse=True))
    
    for j in range(len(arr)-1):
        res = abs(arr[j]-arr[j+1])
        if res not in range(1,4):    
            return inc_or_dec and False
    return inc_or_dec and True

for level in numbers:
    level = list(map(int, level))

    ok = False
    for j in range(len(level)):
        if check_inc_dec(level[:j]+level[j+1:]):
            ok = True

    if ok:
        safe+=1

print("part2 ", safe)
