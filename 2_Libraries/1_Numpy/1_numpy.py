import numpy as np
import time

def time_it(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(f"{func.__name__} Time: {end - start}")
    return wrapper


# Pehle data bana lo (bahar)
a_list = list(range(100000))
b_list = list(range(100000))

a_np = np.arange(100000)
b_np = np.arange(100000)


@time_it
def python_add():
    add = [x+y for x,y in zip(a_list, b_list)]


@time_it
def numpy_add():
    c = a_np + b_np


python_add()
numpy_add()