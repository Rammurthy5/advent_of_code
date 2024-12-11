from functools import cache

with open("11.txt") as f:
    stones = [int(i) for i in f.read().split()]

@cache
def blinkit(stone, steps):
    if steps==0:
        return 1
    if stone==0:
        return blinkit(1, steps-1)
    
    stri = str(stone)
    length = len(stri)

    if length % 2==0:
        return blinkit(int(stri[:length//2]), steps-1) + blinkit(int(stri[length//2:]), steps-1)
    return blinkit(stone*2024, steps-1)


print(sum(blinkit(stone, 75) for stone in stones))