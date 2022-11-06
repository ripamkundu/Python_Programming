n = input("Enter Student Name : ")
c = int(input("C programmin : "))
c1 = int(input("C++ programmin : "))
java = int(input("JAVA ptogramming : "))
php = int(input("PHP programming : "))
python = int(input("Pyhton programming : "))
avg = (c + c1 + java + php + python)/5
print("Total Number : ", avg)

if(avg >= 80):
 print("Grade A")
 
elif(avg >= 90 and avg < 80):
 print("Grade B")

elif(avg >= 60 and avg < 70):
 print("Grade C")

elif(avg >= 40 and avg < 60):
 print("Grade D")
 
elif(avg < 40):
 print("Grade E")
 
else:
 print("Positive Integer.!")