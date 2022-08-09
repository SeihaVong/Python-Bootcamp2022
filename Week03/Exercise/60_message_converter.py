def dec_to_hex(num):
    return hex(num).replace("0x", "")

def message_converter(word):
    res = ""
    for i in word:
        decValue = dec_to_hex(ord(i))
        res += decValue
    return res
print(f"message_converter(“Hello”)")
print(message_converter("Hello").upper())