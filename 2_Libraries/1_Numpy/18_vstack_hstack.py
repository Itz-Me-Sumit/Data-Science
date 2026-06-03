import numpy as np

# vertical stack

a = np.array([1,2,3])
b = np.array([4,5,6])
mat1 = np.vstack((a,b))
print(mat1)


# horizontal stack
c = np.array([
    [1], 
    [2],
    [3] ])
d = np.array([
    [4],
    [5],
    [6]
])
mat2 = np.hstack((c,d))
print(mat2)