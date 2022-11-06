#Numbers Divisible by Another Number

f = int(input("Enter your Frist Number : "))
s = int(input("Enter your second Number : "))
n = f % s
if n == 0:
 print("Result is : " +str(f)+ " is divisible by " +str(s))
else:
 print("Result is : " +str(f)+ " is not divisible by " +str(s))