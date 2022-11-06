import numpy as np
import matplotlib.pyplot as plt
x1= np.arange(0,6*np.pi,0.1)
print(x1)
y1 = np.sin(x1)
plt.plot(x1,y1)
plt.title("Sine Curves")
plt.show()

x= np.arange(0,5*np.pi,0.1)
print(x)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.title("Cosin Curves")
plt.show()




