#Armstrong Number

n = int(input("Enter a number: "))
sum = 0
t = n
while t > 0:
   c = t % 10
   sum = sum + c ** 3
   t = t // 10

if (n == sum):
 print(str(n) + " is an Armstrong number")
else:
 print(str(n) + " is not Armstrong number")