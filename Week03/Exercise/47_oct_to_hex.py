def oct_to_hex(num):
    num = str(num)

    base = 1
    deci = 0
    findoct = int(num) % 10
    if findoct >= 0 and findoct <= 7:
        
        print(f"oct_to_dec({num})")
        while (num):
            remainder = int(num) % 10
            num = int(num) / 10 
            deci += remainder * base 
            base = base * 8 
            
        print(hex(deci).replace("0x",""))
        
    else :
        print("This is not an octal number")
        
oct_to_hex(1271)

