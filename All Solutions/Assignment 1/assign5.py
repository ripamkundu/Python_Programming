#Display Powers of 2 Using Anonymous Function

print(" How Mnay terms you want ?")
t = int(input())
result = list(map(lambda x: 2 ** x, range(t)))
for i in range(t):
   print("2 power of Anonymous Function ",i, "is", result[i])