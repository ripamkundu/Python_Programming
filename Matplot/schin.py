import matplotlib.pyplot as plt
bat = [45, 65, 254, 110, 115, 95, 86, 53, 57, 57, 63, 5,85, 86, 96, 98, 115, 115, 112, 125, 135, 
146, 123, 129, 169, 101, 101, 100, 55, 56, 85, 86, 76, 45, 12, 23, 103, 189, 75, 66, 64, 85]
bins = [ODI, Test_Innings, T20, 50s, 100s]
plt.hist(bat, bins, histtype = 'bar' width = 0.5)
plt.xlabel("Score")
plt.ylabel("Batting Runrate")
plt.title("Schin Batting Score")
plt.show()