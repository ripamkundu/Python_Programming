from heapq import nlargest
list = {"Name":["Sachin","Sourav","Rahul"], "Runs" :[92,96,90]}

print(" My Dictionary :")
print(list, "\n")
Highest = nlargest(8, list, key = list.get)

print(" Highest Runs of the Player :")
for val in Highest:
	print(val, ":", list.get(val))
