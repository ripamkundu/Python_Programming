def circle():
 r =int(input("Enter the Radius : "))
 pi = 3.14
 re = pi * r * r
 print("Area of the circle with the radius :  ", re)

def square():
 s =int(input("Enter the size of a side of a square : "))
 re = s * s 
 print("Area of the square  Is : ", re)

def rectangle():
 l =int(input("Enter the length of the rectangle : "))
 b =int(input("Enter the breadth of the rectangle : "))
 re = l * b 
 print("Area of the rectangle Is : ", re)

while True:
 print("Following Menu : ")
 print("1. Circle") 
 print("2. Square")
 print("3. Rectangle")
 print("4. Exit")
 n=int(input("Enter Your Choice : "))
 if n == 1:
  circle()
 elif n == 2:
  square()
 elif n == 3: 
  rectangle()
 elif n == 4: 
  print("Stop Activity")
  break
 else:
  print("Wrong Input!")
