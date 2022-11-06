import numpy as np
arr = np.array([[10,25,30],
                [42,56,68],
                [22,63,79]])
print("Orginal Array   : ",arr)
print("Determinate Array : ", np.linalg.det(arr))
print("Inverser Matrix : ", np.linalg.inv(arr))