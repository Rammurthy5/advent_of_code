
import re

# Part1
with open("input.txt") as f:
    text = f.readlines()
    
total = 0

for line in text:
    digits = re.findall(r'(\d)', line)
    total += int(digits[0] + digits[-1])

print(total)


# Part2
with open("input.txt") as f:
    text = f.readlines()

total = 0
spelled_digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

for line in text:
    digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    converted_digits = []
    for d in digits:
        converted_digits.append(d if d.isdigit() else spelled_digits[d])
    total += int(converted_digits[0] + converted_digits[-1])

print(total)
