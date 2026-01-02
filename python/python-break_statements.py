import random as r
rand_num = r.randrange(1, 20)
print("Number to be guessed: " , rand_num)
i = 1
while True:
    # print("Number Guesses: ", i)
    if i == rand_num:
        print("Random number guesses is correct")
        break
    i = i + 1
    