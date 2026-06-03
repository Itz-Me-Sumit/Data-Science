import numpy as np

# 1) np.random.rand(shape) -> uniform districution
print(np.random.rand(5,5))

# 2) np.random.randn(shape) -> normal/gaussian distribution
print(np.random.randn(4,3))

# 3) np.random.randint(start , stop , shape)
print(np.random.randint(1,9 , (2,4)))

# 4) np.random.random(shape)
print(np.random.random((3,5)))

# 5) np.random.choice(data , size , replace = True/False)
print(np.random.choice([1,2,3,4] , size = 5))

# 6) np.random.shuffle(data)
arr = np.array([1,2,3,4,5,6])
print(np.random.shuffle(arr))

# 7) np.random.seed(num)
np.random.seed(20)
print(np.random.rand(2,4)) # -> now it'll return always unique values

# 8) np.random.uniform(range , shape)
print(np.random.uniform(1,3 , (2,2)))

# 9) np.random.normal(loc , scale , size)
print(np.random.normal(2 , 2 , (3,4)))