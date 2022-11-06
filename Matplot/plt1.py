import scipy.interpolate as inter
import numpy as np
import matplotlib.pyplot as plt

p, h = list(), list()
print("Pulse vs Height Graph:-\n")
n = input("How many records? ")

print("\nEnter the pulse rate values: ")
for i in range(int(n)):
 pn = input()
 p.append(int(pn))
 x = np.array(p)

print("\nEnter the height values: ")
for i in range(int(n)):
 hn = input()
 h.append(int(hn))
 y = np.array(h)

print("\nPulse vs Height graph is generated!")
z = np.arange(x.min(), x.max(), 0.01)
s = inter.InterpolatedUnivariateSpline(x, y)

plt.plot (x, y, 'b.')
plt.plot (z, s(z), 'g-')
plt.xlabel('Pulse')
plt.ylabel('Height')
plt.title('Pulse vs Height Graph')
plt.show()