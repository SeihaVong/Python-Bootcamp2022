def binToDeci(num):
    
    setB = set(num)
    setforB = {"0","1"}
    
    if setforB == setB or setB == {"0"} or setB == {"1"}:
        return int(num,2)
    
    else:
        print("This is not a binary number")
        
print(binToDeci("110011"))


