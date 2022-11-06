import numpy as np
#(2 x 2) Matrix
a = np.array([[10, 20],
              [15, 20]])
print("Invers Matrix : ")
print(np.linalg.inv(a))  #inv :  inverse matrix

a = np.array([[[10, 20], 
                [15, 20]],
                
             [[-18, 25],
              [30, -45]]]) #inverser several matrix
print("Invers Matrix : ")
print(np.linalg.inv(a))

# (3 x 3) Matrix 
a = np.array([[8, 9, 10],
               [5, 10, -9],
               [-8, 15, 25]])
print("Invers Matrix : ")
print(np.linalg.inv(a)) 