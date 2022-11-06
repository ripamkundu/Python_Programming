import numpy as np
arr = [0,1, 3, 14, 6, 8, 1, 3, 3, 6, 6, 6, 14, 2, 2, 9, 8, 5, 5, 9]
print("Orginal Array : ")
print(arr)
print("Count the number value in each array : ")
print(np.bincount(arr)) #bincount() count number of occurrences of each value