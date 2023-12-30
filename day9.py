def extrapolate(array):
    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[-1] + diff

total = 0

for line in open("day9.txt"):
    nums = list(map(int, line.split()))
    total += extrapolate(nums)

print(total)
