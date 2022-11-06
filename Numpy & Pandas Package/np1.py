import numpy as np
arr = np.array(42)
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2,3],[1,2,3]],[[4,5,6],[7,8,9]]])
print(arr)
print(type(arr))
print(arr.ndim)

print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1.ndim)

print(arr2)
print(type(arr2))
print(arr2.shape)
print(arr2.ndim)

print(arr3)
print(type(arr3))
print(arr3.shape)
print(arr3.ndim)