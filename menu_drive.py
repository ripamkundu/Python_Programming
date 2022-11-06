def armstrong(n):
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
 
 
def krishnamurti(a):
    g= a
    f = 1
    s = 0
    while(a>0):
        r = a%10
        f = 1
        for i in range(1, r+1):
            f = f*i
        s = s+f
        a = a//10
    if(s==g):
        print("it is a krishna murty Number")
    else:
        print("it is not a krishna murty Number")  

    
def compute_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y ==0)):
            lcm = greater 
            break
        greater = greater + 1
    return lcm   

while True:
 print("MENU")
 print("press 1 for armstrong : ")
 print("press 2 for krishnamurthy : ")
 print("press 3 for LCM : ")
 print("press 0 for exit : ")
 print("enter your choice : ")
 
 c=int(input())
 if (c == 1):
    n = int(input("Enter a number: "))
    armstrong(n)
 elif (c == 2):
    print("Eneter a number :")
    a = int(input())
    krishnamurti(a)
 elif (c == 3):
    x=int(input("enter first number : ")) 
    y=int(input("enter second number : "))
    print(" The L.C.M. is : ",compute_lcm(x,y))
    compute_lcm(x,y)
 elif (c == 0):
    print("Thank You, Visit Again..!")
    break 

 else:
   print("Invalid Choice.!")