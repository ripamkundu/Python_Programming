import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100,110,120,150,175,185])
print(arr)
print(arr.shape)
print(type(arr))

newarr = arr.reshape(5,3)
print(newarr)