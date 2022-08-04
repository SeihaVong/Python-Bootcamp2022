def hex_to_oct(num):

    hexdig = set("0123456789abcdef")
    for char in num:
        if (char in hexdig):
            dec = int(num,16)
            print(f'hex_to_dec("{num}")')
            
            
            octal = oct(dec)
            print(octal.replace("0o",""))
            break
            
        else:
            if not (char in hexdig):
                print("This is not a hexa-decimal number") 
                break


hex_to_oct("2b9")