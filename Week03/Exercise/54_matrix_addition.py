matrix1 = [ [10, 5, 4 ,2],
            [5, 0, 9, 5], 
            [9, 19, 60, 8], 
            [7, 8, 4, 5]]

matrix2 = [ [12, 65, 34, 42], 
            [10, 5, 89, 45], 
            [11, 21, 63, 78], 
            [87, 78, 54, 65]]
    
result = [  [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]

def matrix_subtraction(matrix1, matrix2):
    
    result = [[0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
# i = number of arr
# j = number of element in an array
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result
res = matrix_subtraction(matrix1, matrix2)

for i in res:
    print(i)