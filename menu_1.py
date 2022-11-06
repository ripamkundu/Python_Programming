def armstrong(n):
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
 
 
def krishnamurti(n):
 n = int(input("Enter a Number : "))
 g = n
 f = 1
 s = 0
 while(n>0):
        r = n%10
        f = 1
        for i in range(1, r+1):
            f = f*i
        s = s+f
        n = n//10
 if(s==g):
    print("it is a krishna murty Number")
 else:
    print("it is not a krishna murty Number")  
    
    
def palindrom(n):
 n = int(input("Enter a Number : "))
 temp = n
 rev = 0
 while ( n > 0 ):
  digit = n%10
  rev = rev*10+digit
  n = n//10
 if (temp==rev):
  print( " The number is palindrom ! " )
 else:
  print ( "The number is not palindrom ! " ) 


def prime(n):
 n = int(input("Enter a Number : "))
  if n > 1:
   for i in range (2, n):
    if (n % i) == 0:
     print (n,"is not a prime number")
     break
    else:
     print (n," is a prime number")
    else:
     print (n," is not a prime number")   

while(True):
 print("press 1 for armstrong : ")
 print("press 2 for krishnamurti : ")
 print("press 3 for palindrom : ")
 print("press 4 for prime : ")
 print("press 0 for exit : ")
 print("enter your choice : ")
 c=int(input())
 if(c==1):
   armstrong(0)
 elif(c==2):
   krishnamurti(0)   
 elif (c==3):
   palindrom()
 elif (c==4):
   prime(0)   
 else:
  print("Invalid Choice.!")   