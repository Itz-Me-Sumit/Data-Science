import numpy as np

arr = np.array([1,2,3,4,5,3,4,24,12])
print("Mean : ",np.mean(arr) , 3)
print("Median : ",np.median(arr))
print("Standard Deviation : ",np.std(arr))
print("Variance : ",np.var(arr))
print("Min : ",np.min(arr))
print("Index of Min Val : " , np.argmin(arr))
print("Max : ",np.max(arr))
print("Index of Max Val : " , np.argmax(arr))
