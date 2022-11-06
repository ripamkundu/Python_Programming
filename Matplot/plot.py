from matplotlib import style 
style.use('ggplot')
x = np.arange(0,1,0.1)
a = np.sin(x)
b = np.cos(x)
plt.plot(x,a,'r', x,a ,'yo', label = 'x vs a')
plt.plot(x,b,'y',x,b, 'ro', label = 'x vs b')
plt.legend(loc = 'best')
plt.show()
