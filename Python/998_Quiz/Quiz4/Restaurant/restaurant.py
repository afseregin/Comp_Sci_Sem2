import random

restaurants = ["Popeyes", "Chick Fil A", "In n Out"]
Popeyes = ["Chicken Sandwich", "Cajun Fries", "Biscuits"]
ChickFilA = ["Chicken Sandwich", "Waffle Fries", "House Lemonade"]
InnOut = ["Hamburger", "4x4", "Animal Fries"]

restaurant = restaurants[random.randint(0,3)]
print("The restaurant is " + restaurant)

if restaurant == "Popeyes":
    item = Popeyes[random.randint(0,3)]
    print("The menu item is " + item)
    
elif restaurant == "Chick Fil A":
    item = ChickFilA[random.randint(0,3)]
    print("The menu item is " + item)
    
elif restaurant == "In n Out":
    item = InnOut[random.randint(0,3)]
    print("The menu item is " + item)