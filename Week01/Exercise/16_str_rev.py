userInput = input("Enter a string: ")
half1 = userInput[:len(userInput)//2-1:-1]
half2 = userInput[len(userInput)//2:]
print(half1+half2)  