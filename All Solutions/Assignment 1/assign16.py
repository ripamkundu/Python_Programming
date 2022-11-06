#Sum of Natural Numbers Using Recursion

def recursion(n):
   if n <= 1:
       return n
   else:
       return n + recursion(n-1)

num = int(input("Enter a Number : "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is : ",recursion(num))
