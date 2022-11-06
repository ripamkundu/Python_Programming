import numpy as np 
import matplotlib.pyplot as plt
def f(t):
 return np.exp(-t)*np.tan(2*np.pi*t)

t1 = np.arange(1.5,2.5,4)
t2 = np.arange(3.5, 4, 4.5)
t3 = np.arange(4.5, 5, 6.5)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.plot(t2 ,np.tan(2*np.pi*t2))
plt.plot(t3 ,np.sin(2*np.pi*t3))
plt.legend
plt.title("Multiploting")
plt.show()