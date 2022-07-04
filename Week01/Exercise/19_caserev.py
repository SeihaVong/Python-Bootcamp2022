userInput = input("Enter a string: ")
new_str = ""
for i in range(len(userInput)):
    if userInput[i].isupper():
        new_str += userInput[i].lower()
    else:
        new_str += userInput[i].upper()
print(new_str)