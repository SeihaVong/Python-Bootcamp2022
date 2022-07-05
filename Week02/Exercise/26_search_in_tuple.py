def search_in_tuple(tup,search):
    if search in tup:
        return f'element found at index: {tup.index(search)}'  
    else:
        return "element not found in tuple" 
print(search_in_tuple((20,15,10,30),10))
print(search_in_tuple((20,15,10,30),70))
