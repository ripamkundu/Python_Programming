def reverse(s):
      str = " "
      for i in s:
           str = i + str
      return str
s = input("Enter your Name : ")
print("The orginal name is : ",s)
print("The Reverse name is : ",reverse(s))
