import numpy as np
a = np.array([[[12,15,30],[45,96,94]],[[12,19,64],[46,64,54]]])
b = np.array([[[45,96,24],[36,42,74]],[[14,16,64],[64,63,64]]])

print(np.union1d(a,b))
print(np.intersect1d(a,b))
print(np.setdiff1d(a,b))