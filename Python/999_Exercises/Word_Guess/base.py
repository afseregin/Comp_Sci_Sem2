import random

words = []

with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        words.append(l)

f.close()

word = words[random.randint(0,2315)]
for i in range(6):
    while True:
        guess = input("Guess a word ")
        check = 0
        for x in words:
            if guess == x:
                check = 1
        if check == 1:
            break
        else:
            print("Word not in the word list, guess again")
    if guess == word:
        print("Congratulations! You got it")
        break
    else:
        print("Wrong! Guess again")
    for i in word:
        for y in guess:
            if i==y:
                print("The letter "+y+" is correct")
print("The answer is " + word)