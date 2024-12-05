from collections import defaultdict as dd

with open("5.txt") as f:
    input_to_process = [i.strip() for i in f.readlines()]

rule_book_b4 = dd(set)
rule_book_after = dd(set)
total_1 = 0
total_2 = 0


for i in range(len(input_to_process)):
    if input_to_process[i]=='':
        rule_book_index = i
        break
    a,b = input_to_process[i].split("|")
    rule_book_b4[b].add(a)
    rule_book_after[a].add(b)

def check_ordering(pgn):
    correct_order = True
    for i in range(len(pgn)-1):
        if correct_order:    
            for k in range(i+1, len(pgn)):
                if pgn[k] in rule_book_b4[pgn[i]]:
                    correct_order = False
                    break
    return correct_order

def calculate_total(inp_arr):
    dvmd = divmod(len(inp_arr), 2)
    if dvmd[-1]!=0:
        return int(inp_arr[sum(dvmd)-1])

def sort_out_ordering(arr):
    new_page_numbers = []
    for i in range(len(arr)-1):
        for k in range(i+1, len(arr)):
            if arr[k] in rule_book_b4[arr[i]] and arr[k] not in new_page_numbers:
                new_page_numbers.append(arr[k])
        if arr[i] not in new_page_numbers:
            new_page_numbers.append(arr[i])
    if arr[-1] not in new_page_numbers:
        new_page_numbers.append(arr[-1])
    return new_page_numbers

def recurse_part2(arr_2):
    local_arr = sort_out_ordering(arr_2)
    if not check_ordering(local_arr):
        return recurse_part2(local_arr)
    return(calculate_total(local_arr))

for j in range(rule_book_index+1, len(input_to_process)):
    page_numbers = input_to_process[j].split(",")
    
    correct_order = check_ordering(page_numbers) 

    if correct_order:
        total_1+=calculate_total(page_numbers)
    else:
        total_2+=recurse_part2(page_numbers)


print(total_1)
print(total_2)
