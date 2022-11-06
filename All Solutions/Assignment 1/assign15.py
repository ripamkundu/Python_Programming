#Display Fibonacci Sequence Using Recursion

def series(n):
   if n <= 1:
       return n
   else:
       return(series(n-1) + series(n-2))
t = int(input("How Many Element You Want ? "))

if t > 0:
  print("Fibonacci Series Nnmber:")
   for i in range(t):
       print(series(i))
else t <= 0:
   print("Please Enter Positive Integer.!") 