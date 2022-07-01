userInput = input("Enter a string: ")
half1 = userInput[:len(userInput)//2]
half2 = userInput[len(userInput)//2:]
h1Upper = half1.upper()
h2Lower = half2.lower()
print(h1Upper,h2Lower)