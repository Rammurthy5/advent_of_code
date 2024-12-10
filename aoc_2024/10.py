with open("10.txt") as f:
    inp = [list(i.strip()) for i in f.readlines()]

inp = [list(map(int, i)) for i in inp]
rows = len(inp)
cols = len(inp[0])

trailheads = [(r,c) for r in range(rows) for c in range(cols) if inp[r][c]==0]

from collections import deque
total = 0
total_2 = 0

# part 1
for t in trailheads:
    if t[0] < 0 or t[1] < 0 or t[0] >= rows or t[1] >= cols: continue
    que = deque([t])
    checked = {t}
    while len(que)>0:
        r,c = que.popleft()
        for tr, tc in ((r,c+1), (r-1,c), (r+1,c), (r,c-1)):
            if tr<0 or tc<0 or tr>= rows or tc>=cols: continue
            if inp[tr][tc]!=inp[r][c]+1: continue
            if (tr,tc) in checked:
                continue
            checked.add((tr,tc))
            if inp[tr][tc]==9:
                total+=1
            else:
                que.append((tr,tc))

# part 2
for t in trailheads:
    if t[0] < 0 or t[1] < 0 or t[0] >= rows or t[1] >= cols: continue
    que = deque([t])
    checked_2 = {t:1}
    while len(que)>0:
        r,c = que.popleft()
        if inp[r][c]==9:
            total_2+=checked_2[(r,c)]
        for tr, tc in ((r,c+1), (r-1,c), (r+1,c), (r,c-1)):
            if tr<0 or tc<0 or tr>= rows or tc>=cols: continue
            if inp[tr][tc]!=inp[r][c]+1: continue
            if (tr,tc) in checked_2:
                checked_2[(tr,tc)]+=checked_2[(r,c)]
                continue
            checked_2[(tr,tc)]= checked_2[(r,c)]
            que.append((tr,tc))
 
print(total)
print(total_2)