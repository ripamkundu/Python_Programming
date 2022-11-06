#Multiply Two Matrices


X = [[10,25,32],
	[46 ,78,69],
	[77 ,98,85]]

Y = [[45,78,92],
	[15,95,44],
	[39,66,51]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

for i in range(len(X)): 
	for j in range(len(X[0])):
		result[i][j] = X[i][j] * Y[i][j]
for r in result:
	print(r)