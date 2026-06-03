import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# 1) shape
print(arr.shape)

# 2) ndim
print(arr.ndim)

# 3) dtype
print(arr.dtype)

# 4) itemsize
print(arr.itemsize)

# 5) nbyte
print(arr.nbytes)

# 6) Transpose
print(arr.T)