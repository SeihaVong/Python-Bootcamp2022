while True:
    print("press 1 to encode")
    print("press 2 to decode")
    press = int(input(""))
    if press == 1:
        word = input("Enter the string to encode: ")
        deword = ''
        for word in word:
            word = ord(word)
            if word >= 65 and word <= 77 or word >= 97 and word <= 109:
                word += 13
                word = chr(word)
                deword +=  word
            elif word >= 78 and word <= 90 or word >= 110 and word <= 122:
                word -= 13
                word = chr(word)
                deword += word
        print(f'The decode text is: {deword}')
    else:
        word = input("Enter the string to decode: ")
        deword = ''
        for word in word:
            word = ord(word)
            if word >= 65 and word <= 77 or word >= 97 and word <= 109:
                word += 13
                word = chr(word)
                deword += word
            elif word >= 78 and word <= 90 or word >= 110 and word <= 122:
                word -= 13
                word = chr(word)
                deword += word
        print(f'the decode text is: {deword}')
    print("Do you want to continue?(Y/N)")
    next = input("")
    if next == "N":
        break
