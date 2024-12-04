
with open("4.txt") as f:
    content = [i.strip() for i in f.readlines()]

# part 1
row = len(content)
col = len(content[0])

total_1 = 0
total_2 = 0


for r in range(row):
    for c in range(col):
    # part 1    
    # reverse and straight in the same row
    # reverse and straight in the same col
    # reverse and straight in forward diagonal
    # reverse and straight in backward diagonal

        if (c+3) < col:
            if "XMAS" in content[r][c]+content[r][c+1]+content[r][c+2]+content[r][c+3]:
                total_1+=1
            if "SAMX" in content[r][c]+content[r][c+1]+content[r][c+2]+content[r][c+3]:
                total_1+=1
        if (r+3) < row:
            if "XMAS" in content[r][c]+content[r+1][c]+content[r+2][c]+content[r+3][c]:
                total_1+=1
            if "SAMX" in content[r][c]+content[r+1][c]+content[r+2][c]+content[r+3][c]:
                total_1+=1
        if (r+3) < row and (c+3) < col:
            if "XMAS" in content[r][c]+content[r+1][c+1]+content[r+2][c+2]+content[r+3][c+3]:
                total_1+=1
            if "SAMX" in content[r][c]+content[r+1][c+1]+content[r+2][c+2]+content[r+3][c+3]:
                total_1+=1
        if (r-3) >= 0 and (c+3) < col:
            if "XMAS" in content[r][c]+content[r-1][c+1]+content[r-2][c+2]+content[r-3][c+3]:
                total_1+=1
            if "SAMX" in content[r][c]+content[r-1][c+1]+content[r-2][c+2]+content[r-3][c+3]:
                total_1+=1
        
        # part 2
        if (c+2) < col and (r+2) < row:
            if content[r][c]+content[r+1][c+1]+content[r+2][c+2] in ("MAS", "SAM") and \
            content[r+2][c]+content[r+1][c+1]+content[r][c+2] in ("MAS", "SAM"):
                total_2+=1
        
            
            
print(total_1)
print(total_2)
