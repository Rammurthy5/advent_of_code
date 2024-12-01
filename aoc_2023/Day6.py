with open("day6_input.txt") as f:
    text = f.readlines()

# part 1
time_array = map(lambda x:int(x), text[0].split("Time:")[-1].split())
distance_array = map(lambda x:int(x), text[1].split("Distance:")[-1].split())

cumulative_resp = 1
for t, d in zip(time_array, distance_array):
    local_sum = 0
    speed_per_ms = round(d/t)
    if (d/t) - speed_per_ms < 0.51:
        speed_per_ms+=1

    for i in range(speed_per_ms, (t - speed_per_ms)+1):
        if (t - i) * i > d:
            local_sum+=1

    cumulative_resp *= local_sum

print(cumulative_resp)

#part 2

time = int(text[0].split("Time:")[-1].replace(' ',''))
distance = int(text[1].split("Distance:")[-1].replace(' ',''))

cumulative_resp = 0
speed_per_ms = round(distance/time)
if (distance/time) - speed_per_ms < 0.51:
    speed_per_ms+=1

for i in range(speed_per_ms, (time - speed_per_ms)+1):
    if (time - i) * i > distance:
        cumulative_resp+=1

print(cumulative_resp)
