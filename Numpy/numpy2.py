import numpy as np
a = np.array({42})
b = np.array([10,20,30])
f = np.array((10,56,89,86))
c = np.array([[10,20,30],[40,50,60]])
d = np.array([[[12,45,85],[86,36,56]],[[36,24,65],[63,84,76]]])
e = np.array([10,20,30,45,86,96,78,96,86,74,56,96,82,45,78,32,12,45,82,80,10,54,63,89,63,78,63,64,86,10])


print(a)
print(a.ndim)
print(type(a))

print(b)
print(b.ndim)
print(type(b))

print(f)
print(f.ndim)
print(type(f))

print(c)
print(c.ndim)
print(type(c))

print(d)
print(d.ndim)
print(type(d))

print(e)
print(e.ndim)
print(type(e))

newe = e.reshape(10,3)
print(newe)
print(newe.ndim)

