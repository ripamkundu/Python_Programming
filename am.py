n = int(input("Enter a number : "))
sum = 1
t = n
while(t>0):
    c = t %10
    sum = sum + c**3
    t  = t//10
if(n==sum):
    print("Amstrong number"+str(n))
else:
    print("not amstrong number"+str(n))
