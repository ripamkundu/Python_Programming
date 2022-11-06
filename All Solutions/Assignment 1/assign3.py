#Aramstrong Number Interval

l = int(input("Enter Lower Number Interval : "))
u = int(input("Enter upper Number Interval : "))
for n in range(l,u+1):
 order = len(str(n))
 sum = 0
 t = n
 while t > 0:
  c = t % 10
  sum = sum + c ** 3
  t = t // 10
 if (n == sum):
  print(n)