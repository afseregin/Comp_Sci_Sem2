items = []
price = []
quantity = int(input("How many items are you purchasing? "))
for x in range(quantity):
    name = input("What item are you purchasing? ")
    cost = int(input("How much does it cost? "))
    print("Thank you for purchasing: " + name)
    items.append(name)
    price.append(cost)
print("Thank you for purchasing: ")
for x in items:
    print(x)
print("Your total comes out to: " , end="")
total = 0
for x in price:
    total = total+x
print(total)