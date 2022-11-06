#GCD

def gcd(x,y):
 if(y==0):
  return x 
 else:
  return gcd (y,x%y)
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
n= gcd(x,y)
print("GCD Result Is : " +str(n))