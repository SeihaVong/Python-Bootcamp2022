from bdb import Breakpoint


def hex_to_dec(num):
    hexDigits = set("0123456789abcdef")
    num = str(num)
    decimal = int(num,16)
    for char in num:
        if (char in hexDigits):
            print(f'hex_to_dec("{num}")')
            print(decimal)
            break
            
        else:
            if char in hexDigits:
                print("This is not a hexa-decimal number")
                Breakpoint

hex_to_dec("ba1")