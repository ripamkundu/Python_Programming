#Factors Of Number

n = int(input("Enter a Number : "))
print("Factors Of Number is "+str(n))
for i in range(1,n+1):
 if n%i==0:
  print(i)