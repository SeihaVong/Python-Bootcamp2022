import random
userInput = int(input("Input a number:"))
sum = 0
for i in range(userInput):
    random_num = random.randint(2000,3000)
    if random_num % 2 == 0:
        sum += random_num
        print(sum)