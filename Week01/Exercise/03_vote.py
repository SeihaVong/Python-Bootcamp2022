userInput = int(input("Input your age:"))

if userInput >= 18:
    print("You are eligible for vote")
elif userInput < 18 and userInput >=1:
    print("You aren't adult yet... Sorry can't vote")
else:
    print("Age must be positive digit")