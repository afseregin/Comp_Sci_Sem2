symbol = input("What is the symbol?")
width = int(input("What is the width?"))
height = int(input("What is the height?"))

for y in range(height):
    for x in range(width):
        print(symbol, end = "")
    print("")