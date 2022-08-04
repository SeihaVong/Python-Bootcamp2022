def bin_to_hex(num):
    num = str(num)
    SetBin = set(num)
    setForBin = {"0","1"}

    if setForBin == SetBin or SetBin == {"0"} or SetBin == {"1"}:
        print(f"bin_to_oct({num})")
        decimal = int(num,2) 
        print(hex(decimal).replace("0x",""))
        
    else:
        print("This is not binary number")

bin_to_hex(11001101)