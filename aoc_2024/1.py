with open("1.txt") as f:
    numbers = [l.split() for l in f.readlines()]

list1, list2 = [],[]

for n in numbers:
    list1.append(int(n[0]))
    list2.append(int(n[1]))

list1 = sorted(list1)
list2 = sorted(list2)

# Part 1
total = 0
for c,d in zip(list1, list2):
    total+=abs(c-d)

print(total)

# Part 2
total_2 = 0
from collections import Counter
c = Counter(list2)
for e in list1:
    total_2+=e*c[e]

print(total_2)