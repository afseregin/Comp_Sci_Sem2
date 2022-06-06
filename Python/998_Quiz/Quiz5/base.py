number = input("What is your favorite number?")
age = int(input("What is your age"))

for i in range(len(number)):
    if number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="8" or number[i]=="9" or number[i]=="0":
        number = number[i:len(number)]
        break
print(int(number)* age)