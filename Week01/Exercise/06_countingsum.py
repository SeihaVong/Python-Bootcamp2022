sum = 0
while True:
    userInput = input("Input a Number:")
    if userInput =='stop':
        break
    else:
        if userInput.isdecimal():
            sum += int(userInput)
        else:
            print("The input must be a valid number")
            
print(f'sum = {sum}')
