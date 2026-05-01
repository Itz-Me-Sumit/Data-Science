import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr[0] , arr[-1] , arr[::-1])

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


"""
    matrix[row , column]
    matrix[row]
"""


print(matrix[0,2])
print(matrix[1])

# access perticular rows
print('first row' , matrix[0])
print('second row' , matrix[1])
print('third row' , matrix[2])

# access perticular columns
print('first column' , matrix[:: , 0])
print('second column' , matrix[:: , 1])
print('third column' , matrix[:: , 2])


# reverse the rows of matrix
print(matrix[::-1])

# reverse the columns of matrix
print(matrix[:: , ::-1])

# reverse whole matrix
print(matrix[::-1 , ::-1])

# conditional Indexing
arr2 = np.array([31,3,11,34,81,9,21,52,6])
print( arr2[arr2>10] )

# custom index
idx = [2,3,5]
print(arr2[idx])

# get index where condition satisfies
index = np.where(arr2>20)
print(index)
