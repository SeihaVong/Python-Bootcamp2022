def oct_to_hex(num):
    print(f"oct_to_hex({str(num)})")
    if not int(num):
        print("a valid octal number")
        return
    if str(num).find("8")>=1 or str(num).find("9")>=1:
         print("this is not a octal number")
         return
    else:
        num=int(num)
        decimal_value = 0
        base = 1
        while (num):
            last_digit = num % 10
            num = int(num / 10)
            decimal_value += last_digit * base
            base = base * 8
        print(decimal_value)

oct_to_hex(750)