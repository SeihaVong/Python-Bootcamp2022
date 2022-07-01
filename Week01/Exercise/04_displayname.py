userInput = input("Input your name:")
times = int(input("Input number of time to print: "))

if userInput == '':
    print("No name entered")
else:
    for i in range(times):
        print(userInput)
    