def dec_to_bin(num):
    return bin(num).replace("0b", " ")


def binary_addition(num1, num2):
    toBin1 = str(dec_to_bin(num1));
    toBin2 = str(dec_to_bin(num2));
    return bin(int(toBin1,2) - int(toBin2,2)).replace("0b", " ")


print(f"Binary: {binary_addition(60, 50)}")


def binaryToDecimal(n):
    return int(n,2)
 
print(f"Decimal: {binaryToDecimal(binary_addition(60, 50))}")