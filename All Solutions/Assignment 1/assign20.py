#Transpose a Matrix

n = 4
def transpose(x,y):
 for i in range(n):
  for j in range(n):
   y[i][j] = x[j][i]
x =[[1, 5, 9, 7],
     [9, 6, 2, 8],
     [5, 4, 8, 9],
     [3, 4, 8, 6]]
     
y =  [[0,0,0, 0],
		[0,0,0, 0],
		[0,0,0, 0],
        [0, 0, 0, 0]]
transpose(x, y)
print("Result is : ")
for i in range(n):
 for j in range(n):
  print(y[i][j], " " ,  end = ' ')
 print()
  