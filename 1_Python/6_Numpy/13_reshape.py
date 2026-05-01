import numpy as np

# rehshape
arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped1 = arr3.reshape(3,4)
print(reshaped1)
reshaped2 = arr3.reshape(4,3)
print(reshaped2)


# flatten
arr4 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
print(arr4.flatten())

# resize
arr4.resize(2,6)
print(arr4)

# squeeze
arr5 = [[[3],[4],[7]] , [[3],[4],[7]]]
print(np.squeeze(arr5))