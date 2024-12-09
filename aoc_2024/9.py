with open("9.txt") as f:
    inp = f.read().strip()

formed_disk_block = ''

c = inp[0]
occupied_digit = 0
free_space_dot = '.'
first_free_space_ind = 0
length_of_inp = len(inp)
total = 0

for ind, i in enumerate(inp):
    if ind % 2 ==0:
        formed_disk_block+=int(i)*str(occupied_digit)
    else:
        occupied_digit+=1
        formed_disk_block+=int(i)*free_space_dot
formed_disk_block = list(formed_disk_block)

right_cursor = len(formed_disk_block)-1

for j in range(len(formed_disk_block)):
    if j >= right_cursor:
        break
    if formed_disk_block[j]=='.' and formed_disk_block[right_cursor]!='.':
        formed_disk_block[j], formed_disk_block[right_cursor] = formed_disk_block[right_cursor], formed_disk_block[j]
        right_cursor-=1
    elif formed_disk_block[j]=='.'==formed_disk_block[right_cursor]:
        while formed_disk_block[right_cursor]=='.':
            right_cursor-=1
        formed_disk_block[j], formed_disk_block[right_cursor] = formed_disk_block[right_cursor], formed_disk_block[j]
        right_cursor-=1

print(len(formed_disk_block))

for ind, k in enumerate(formed_disk_block):
    if k=='.':
        print(ind)
        break
    total+=(ind*int(k))

print(total)