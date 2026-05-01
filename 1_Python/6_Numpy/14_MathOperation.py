import numpy as np

# add
a = np.array([1,2,3])
b = np.array([9,1,4])
print(a+b)

# substract
print(a-b)

# multiplication
print(a*b)

# division
print(a/b)


# matrix-multiplication
mat1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
mat2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(mat1@mat2)

# comparison
print(a>b , a<b)