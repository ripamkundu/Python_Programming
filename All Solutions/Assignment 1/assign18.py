#Convert Decimal to Binary Using Recursion

def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')
   
num = int(input("Enter a Number : "))
binary(num)