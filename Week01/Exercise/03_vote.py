userInput = int(input("Input your age:"))

if userInput >= 18:
    print("You are eligible for vote")
elif userInput < 18 and userInput >=1:
    print("You aren't adult yet... Sorry can't vote")
# elif userInput < 0:
else:
    print("Age must be positive digit")