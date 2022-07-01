num = input("Input a number:")
oddNum = 0
evenNum = 0
if num.isdecimal():
    for i in range(int(num)+1):
        if i % 2 == 0:
            evenNum += i
        else:
            oddNum += i 
    print(f"Sum of odd numbers = {evenNum}")
    print(f"Sum of odd numbers = {oddNum}")
else:
    print("Invalid input")
    print(f"Sum of odd numbers = 0")
    print(f"Sum of odd numbers = 0")
    