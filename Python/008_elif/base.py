num = int(input("What is the first number?"))
operation = input("What is the operation?")
num2 = int(input("What is the second number?"))

print(str(num) + operation + str(num2) + "=")

if operation=="+":
    print(num+num2)
elif operation=="-":
    print(num-num2)
elif operation=="/":
    print(num/num2)
elif operation=="*":
    print(num*num2)