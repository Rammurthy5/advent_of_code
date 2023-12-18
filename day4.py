import re
cumulative_sum = 0
with open("day4_input.txt") as f:
    text = f.readlines()

for line in text:
     numbers = line.split(":")[-1].strip().split("|")
     array1, array2 = [n.split() for n in numbers]
     
     local_sum = 0
     for a in array2:
          if a in array1:
               if local_sum == 0:
                    local_sum += 1
               else:
                    local_sum +=local_sum
     
     cumulative_sum +=local_sum
     
print(cumulative_sum)

# Part2
cumulative_array =[1] * len(text)
for ind, line in enumerate(text):
     numbers = line.split(":")[-1].strip().split("|")
     array1, array2 = [n.split() for n in numbers]
     local_sum=0
     for a in array2:
          if a in array1:
               local_sum+=1

     for j in range(ind+1, ind+local_sum+1):
        cumulative_array[j]+=cumulative_array[ind]
     
print(sum(cumulative_array))
