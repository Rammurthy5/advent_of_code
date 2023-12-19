import re

with open("day5_input.txt") as f:
    text = f.read()


# Extract seeds
seeds_match = re.search(r"seeds: (.+)", text)
seeds = list(map(int, seeds_match.group(1).split()))

# Extract maps using regex
maps = re.findall(r"([a-z]+-to-[a-z]+ map:)(.+?)(?=[a-z]+-to-[a-z]+ map:|$)", text, re.DOTALL | re.IGNORECASE)

# Define map names
map_names = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water",
             "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

# Create a dictionary to store the maps
map_dict = {}

# Process each map and convert the numbers to a list of lists
for name, values in zip(map_names, maps):
    map_dict[name] = [list(map(int, line.split())) for line in values[1].strip().split('\n')]

# Part1
lowest_location = float('inf')

def matcher(s, map):
    for j in map_dict[map]:
        dest, src, length = j
        if s in range(src, src+length):
            return dest+abs(src-s)

    return s

for s in seeds:
    soil = matcher(s, map_names[0])
    fertilizer = matcher(soil, map_names[1])
    water = matcher(fertilizer, map_names[2])
    light = matcher(water, map_names[3])
    temp = matcher(light, map_names[4])
    humidity = matcher(temp, map_names[5])
    location = matcher(humidity, map_names[6])
    lowest_location = min(lowest_location, location)


print(lowest_location)

# Part 2 
q = { 5: text.strip()}
sections = re.split(r'\n\n', q[5].strip())
seeds = list(map(int, sections[0].split()[1:]))
maps = sections[1:]

current = [(a,a+b) for a,b in zip(seeds[::2], seeds[1::2])]

for table in maps:
    rows = [tuple(map(int, row.split())) for row in table.split('\n')[1:]]
    i_start = [-99]
    offsets = [0]
    latest_end = -99
    for row in sorted(rows, key=lambda row: row[1]):
        latest_end = max(latest_end, row[1]+row[2])
        offset = row[0] - row[1]
        if i_start and i_start[-1] == row[1]:
            i_start[-1] = row[1]
            offsets[-1] = offset
        else:
            i_start.append(row[1])
            offsets.append(offset)
        i_start.append(row[1]+row[2])
        offsets.append(0)

    out = []
    
    for interval in current:
        splits = [interval[0]]
        start_index = None
        for idx, post in enumerate(i_start):
            if post <= splits[-1]:
                continue
            if start_index is None:
                start_index = idx - 1
            if post < interval[1]:
                if post != interval[1]:
                    splits.append(post)
            else:
                break
        splits.append(interval[1])
        start_index = start_index or len(offsets)
        for a,b in zip(splits, splits[1:]):
            dx = offsets[min(start_index or float('inf'), len(offsets)-1)]
            start_index += 1
            out.append((a+dx, b+dx))
        
    current = out
    
print('Day 05 Part 2:',min(c[0] for c in current))
