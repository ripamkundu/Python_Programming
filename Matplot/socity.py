import numpy as np
import matplotlib.pyplot as plt
data = [[10, 20, 25, 27],
        [27, 30, 37, 40],
        [874, 46, 35, 12],
        [19, 39, 46, 28]]
x = np.arange(4)
fig = plt.figure()
ax = fig.add([0,0,1,1])
ax.bar(x + 0.00, data[0], color = 'r', width = 0.30)
ax.bar(x + 0.25, data[1], color = 'y', width = 0.30)
ax.bar(x + 0.50, data[2], color = 'b', width = 0.30)
ax.bar(x + 0.75, data[3], color = 'g', width = 0.30)
plt.xlabel('Richest')
plt.ylabel('Provarty')
plt.title('Socity Information')
plt.show()