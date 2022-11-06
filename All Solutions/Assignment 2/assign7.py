#reverse Number

num = int(input("Enter a Number You want to reverse : "))
rev = 0
while num > 0:
  rem = num % 10  
  rev = (rev*10) + rem
  num = num//10  
print("Number Is : " +str(rev))