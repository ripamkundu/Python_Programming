#covariance of matix
import numpy as np
a = np.array([[10, 17, 21],   #Assign positive Integer
               [27, 39, 46],
               [55, 65, 79]])
               
b = np.array([[-12, -19, -21],  #Assign Negative Integer
               [-29, -34, -47],
               [-57, -69, -73]])

print("Orginal Array : ")  
print(a)             
print("Co-variance Number : ")
print(np.cov(a))  #cov : covariance Function

print("Orginal Array : ")  
print(b) 
print("Co-variance Number Negative Integer [ - ] : ")
print(np.cov(b))     #Negative Integer

print("Co-variance matix of two given array  [a , b] : ")
print(np.cov(a, b))
