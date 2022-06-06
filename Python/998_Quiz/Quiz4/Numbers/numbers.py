mynumbers = [6,9,32,28,15,22,3,18]

min = mynumbers[0]
for i in mynumbers:
    if i<min:
        min = i
print(min)

max = mynumbers[0]
for i in mynumbers:
    if i>max:
        max = i
print(max)

average = 0
count = 0
for i in mynumbers:
    average= average+i
    count = count+1
average = average/count
print(average)