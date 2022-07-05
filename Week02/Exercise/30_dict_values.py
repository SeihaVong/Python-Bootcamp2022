def dict_value(dict):
    count = 0
    for key, value in dict.items():
        print(key , ":" , *value)
        if count != len(dict):
            print("*" * 5)
            count += 1
            
(dict_value({
            120: ("Visal", "Borey", "Sovann"),
            130: ("Hout","Mouyleng","Pidor"),
            140: ("Nary", "Misora", "Masaaki"),     
            })) 