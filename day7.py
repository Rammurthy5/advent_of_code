from collections import Counter

with open("day7_input.txt") as f:
    text = f.readlines()

rank_dict = {"five": [], "four": [], "three":[], "two": [], "one":[], "fullhouse": [], "highcard":[]}

for line in text:
    strng, bid = line.split()
    strng = strng.replace("A", "E")
    strng = strng.replace("K", "D")
    strng = strng.replace("Q", "C")
    strng = strng.replace("J", "B")
    strng = strng.replace("T", "A")
        
    count_dict = Counter(strng)
    if len(count_dict)==1:
        rank_dict["five"].append((strng, int(bid)))
    elif len(count_dict)==5:
        rank_dict["highcard"].append((strng, int(bid)))
    elif len(count_dict)==4:
        rank_dict["one"].append((strng, int(bid)))
    elif len(count_dict)==2:
        if 3 in list(count_dict.values()):
            rank_dict["fullhouse"].append((strng, int(bid)))
        else:
            rank_dict["four"].append((strng, int(bid)))
    else:
        if 3 in list(count_dict.values()):
            rank_dict["three"].append((strng, int(bid)))
        else:
            rank_dict["two"].append((strng, int(bid)))


cumulative_sum = 0
length = len(text)
   
for v in ["five", "four", "fullhouse", "three", "two", "one", "highcard"]:
    data = sorted(rank_dict[v], key=lambda x: x[0], reverse=True)
    for i in data:
        cumulative_sum += (length * i[-1])
        length -=1

print(cumulative_sum)
        
