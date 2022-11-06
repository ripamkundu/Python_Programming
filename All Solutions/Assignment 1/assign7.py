#Convert Decimal to Binary, Octal and Hexadecimal 

n = int(input("Enter a Decimal Number : "))

print("1.Decimal to Binary")
print("2.Decimal to Octal")
print("3. Decimal to Hexadecimal")

c = int(input("Enter Your choice : "))
if c==1:
 print("Binary Number : ",bin(n))
elif c==2:
 print("Octal Number : ",oct(n))
elif c==3:
 print("Hexadecimal Number : ",hex(n))
else:
 print("Enter Positive integer.")