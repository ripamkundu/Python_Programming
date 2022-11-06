#sum of natural number

n = int(input("Enter a Number : "))
if (n >0):
 sum = 0
 while(n>0):
  sum = sum + n
  n = n - 1
  print("Result is : "+str(sum))
 
else:
 n <= 0
 print("Enter The positive integer.!")