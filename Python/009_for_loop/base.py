length = int(input("What is the line length?"))
direction = input("Vertical or Horizontal?")

if direction=="vertical":
    for x in range(length):
        print("*")
if direction=="horizontal":
    for x in range(length):
        print("*", end = "")