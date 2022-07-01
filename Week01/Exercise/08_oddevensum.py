num = input("Input a number:")
oddNum = 0
evenNum = 0
countEven = 0
countOdd =0
if num.isdecimal():
    for i in range(int(num)+1):
        if i % 2 == 0:
            evenNum += i
            countEven += 1
        else:
            oddNum += i 
            countOdd += 1
    print(f"Average of even numbers = {evenNum/countEven}")
    print(f"Average of odd numbers = {oddNum/countOdd}")
else:
    print("Invalid input")