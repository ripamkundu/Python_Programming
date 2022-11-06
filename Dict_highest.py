from heapq import nlargest
list = {'Virat Kholi': 152, 'Rohit Sharma': 83, 'Rishav Pant': 75,
		'M.S Dhoni': 56, 'Ravindra Jadeja': 42, 'Bhumrah': 69,
		'Shaker Dhawan' : 74, 'KL Rahul' : 59}

print(" My Dictionary :")
print(list, "\n")
Highest = nlargest(8, list, key = list.get)

print(" Highest Runs of the Player :")
for val in Highest:
	print(val, ":", list.get(val))
