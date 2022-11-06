import matplotlib.pyplot as plt 
labels = ['Cookies', 'jellybean', 'Milkshake', 'Cake']
size = [38.5, 40.6, 52.8, 22.6]
colors =['yellow', 'red', 'blue', 'green']
patches, texts = plt.pie(size, colors=colors, startangle = 90)
plt.legend(patches, labels, loc = "best")
plt.xlabel('Days')
plt.ylabel('Info')
plt.title('Cooking Information')
plt.show()