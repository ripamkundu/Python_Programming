n = int(input("Enter the maximum Number : "))
t= 0
for i in range(1, n+1):
     if(i %2 == 0):
           print("{0}".format(i))
           t = t+i
print("Sum of Even Number 1 to {0} = {1}".format(i,t))