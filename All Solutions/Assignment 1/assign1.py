#Fobibonacci series

n=int(input("Enter Number of series : "))
x=0
y=1
z=0
if (n<=0):
 print("Enter the positive integer")
else:
 for i in range(0,n):
  x = y 
  y = z 
  z = x+y
  print(z)
