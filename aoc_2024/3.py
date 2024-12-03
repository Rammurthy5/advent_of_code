import re
import math

exp  = re.compile(r'mul\(\d+\,\d+\)')

with open("3.txt") as f:
    content = f.read()
# sample content = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# part 1
mul_array = exp.findall(content)

total = 0

for i in mul_array:
    total+=math.prod(map(int,re.findall("\d+",i)))

print(total)

# part 2
# sample content = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
total=0
do_flag=True

for i in range(len(content)):
    if content[i:].startswith("do()"):
        do_flag = True
    elif content[i:].startswith("don't()"):
        do_flag = False

    if do_flag:
        matched_numbers = exp.match(content[i:])
        if matched_numbers is not None:
            get_ints = re.findall(r'\d+',matched_numbers.group(0))
            if get_ints:
                total+=math.prod(map(int,get_ints))
print(total)
