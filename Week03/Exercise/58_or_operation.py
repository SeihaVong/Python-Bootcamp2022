def hextobin(h):
  return bin(int(h, 16))[2:].zfill(len(h))
  
def bintoDec(n):
    return int(n,2)

def or_operation(num1, num2):
    # convert hexadecimal to binary
    binNum1 = str(hextobin(num1));
    binNum2 = str(hextobin(num2));

    # convert binary to decimal
    deciNum1 = bintoDec(binNum1)
    deciNum2 = bintoDec(binNum2)
    print(binNum1) 
    print(binNum2)
    return bin(deciNum1 | deciNum2).replace("0b", "")

print(or_operation("33", "3D"))