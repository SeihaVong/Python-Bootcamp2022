userInput = input("Input a number: ")
if userInput.isdecimal():
    userInput = int(userInput)
    if userInput % 2 == 1:
        print("Odd number")
    elif userInput % 2 == 0:
        print("Even number")
else:
    print("Not a valid number")