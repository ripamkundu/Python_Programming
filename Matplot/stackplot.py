import matplotlib.pyplot as plt
play = [10, 15, 20, 25, 30, 35, 40]
python = [2, 8, 10, 15, 17, 20, 21]
java = [15, 17, 20, 28, 30, 25, 24]
c = [20, 65, 12, 16, 27, 29, 30]
css = [8, 12, 17, 18, 19, 26, 37]
php = [0, 2, 6, 5, 7, 7.5, 6]

plt.plot([], [], color = 'b', label = 'play', linewidth = 5)
plt.plot([], [], color = 'r', label = 'python', linewidth = 5)
plt.plot([], [], color = 'm', label = 'java', linewidth = 5)
plt.plot([], [], color = 'k', label = 'c', linewidth = 5)
plt.plot([], [], color = 'y', label = 'css', linewidth = 5)
plt.plot([], [], color = 'c', label = 'php', linewidth = 5)

plt.stackplot(play, python, java, c, css, php, color = ['b', 'r', 'm', 'k', 'y', 'c'])
plt.xlabel('X Axis')
plt.ylabel('y Axis')
plt.title('Stack ploting')
plt.legend()
plt.show()