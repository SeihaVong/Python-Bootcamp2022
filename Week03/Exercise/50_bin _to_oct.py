def bin_to_oct(num):
    num = str(num)
    setBin = set(num)
    setForBin = {"0","1"}

    if setForBin == setBin or setBin == {"0"} or setBin == {"1"}:
        print(f"bin_to_oct({num})")
        decimal = int(num,2)
        print(oct(decimal).replace("0o","")) 
        
    else:
        print("This is not binary number")

bin_to_oct(11001101)