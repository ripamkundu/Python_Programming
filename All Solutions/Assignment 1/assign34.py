#Make a Flattened List from Nested List

list = [[10], [20, 30], [40, 50, 60, 70]]

list = [num for sublist in list for num in sublist]
print(list)