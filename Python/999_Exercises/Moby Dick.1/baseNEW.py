# sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
# word = ""
# counter = 0

# for x in range(len(sentence)):
#     word = word + sentence[x]
#     if sentence[x]==" ":
#         if "whale" in word or "Whale" in word:
#             counter=counter+1
#             word = ""
# print(counter)








with open('moby.txt') as f:
    counter = 0
    for line in f:
        sentence = line.strip()
        word = ""
        
        for x in range(len(sentence)):
            word = word + sentence[x]
            if sentence[x]==" ":\\\\\\\\\\\\\\\\\   
                if "whale" in word or "Whale" in word:
                    counter=counter+1
                    word = ""
    print(counter)

f.close()
