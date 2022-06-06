import random

x = int(input("How many random numbers would you like?"))
numbers = []
for i in range(x):
    numbers.append(random.randrange(10))
y = 0
for i in numbers:
    print(str(i),end = "")
    if y==x-1:
        break
    print(",",end="")
    y=y+1