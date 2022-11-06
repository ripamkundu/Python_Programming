import matplotlib.pyplot as plt
sourav = ["ODI", "Test Innings", "T20", "ODI 50s", "ODI 100s"]
s = [4563, 3692, 1264, 86, 56]
plt.bar(sourav, s, width = .5)
plt.xlabel("Score")
plt.ylabel("Batting Rate")
plt.title("Sourav Gangully")
plt.show()