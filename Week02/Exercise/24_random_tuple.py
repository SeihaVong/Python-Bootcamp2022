import random
def random_tuple(num):
    list1 = []                    
    sum = 0
    for i in range(num):               
        random_num = random.randint(0,100)              
        print(f'Random number{i+1}: {random_num}')               
        sum += random_num                      
        list1.append(random_num)                              
    print(tuple(list1))
    return sum
            
print(random_tuple(5))

        
