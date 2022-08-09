# matrix1 = [ [3, 7, 5],
#             [2, 6 ,7], 
#             [4, 3, 2], ]

# matrix2 = [ [6, 5, 4], 
#             [3, 2, 1], 
#             [1, 2 ,3],]
    

# def matrix_multiplication(matrix1, matrix2):
#     result = [[0, 0, 0], 
#             [0, 0, 0], 
#             [0, 0, 0]]
#     for i in range(len(matrix1)):
#         for j in range(len(matrix2[0])):
#             for k in range(len(matrix2)):
#                 result[i][j] += matrix1[i][k] * matrix2[k][j]
#     return result
# res = matrix_multiplication(matrix1, matrix2)
# for i in res:
#     print(i)
    
matrix1 = [ [10, 5, 4 ,2],
            [5, 10, 9, 55], 
            [9, 19, 69, 8], 
            [7, 8, 4, 75]]

matrix2 = [ [12, 65, 34, 2], 
            [1, 5, 8, 45], 
            [7, 21, 63, 8], 
            [0, 78, 4, 65]]


def matrix_subtraction(matrix1, matrix2):
    
    result = [[0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result
res = matrix_subtraction(matrix1, matrix2)

for i in res:
    print(i)