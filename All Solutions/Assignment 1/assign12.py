#Simple Calculator

def add(x,y):
 return x + y 
 
def substract(x,y):
 return x - y
 
def division(x,y):
 return x / y 
 
def Multiplication(x,y):
 return x * y
 
f = int(input("Enter Frist Number : ")
s = int(input("Enter Second Number : "))
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
c = int(input("Enter Your Choice : "))
if c==1:
 print(str(f) + " + " + str(s)+ " = ", add(f,s)) 
elif c==2: 
 print(str(f) + " + " + str(s)+ " = ", substract(f,s))
elif c==3: 
 print(str(f) + " + " + str(s)+ " = ", division(f,s))  
elif c==4: 
 print(str(f) + " + " + str(s)+ " = ", Multiplication(f,s)) 
else:
 print("Invalid Choice")

