name = input("What is your first and last name?")
first = ""


for x in range(len(name)):
    first = first + name[x]
    if name[x] == " ":
        for y in range(x+1,len(name)):
            print(name[y])
        break
print(" ")
for x in first:
    print(x)