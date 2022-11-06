n = input("Enter Student Name : ")
c = int(input("C programmin : "))
c1 = int(input("C++ programmin : "))
java = int(input("JAVA ptogramming : "))
php = int(input("PHP programming : "))
python = int(input("Pyhton programming : "))
avg = (c + c1 + java + php + python)/5
print("Total Number : ", avg)

if(avg >= 90):
 print("Grade A+")
 print("CGPA : 9")
 
elif(avg < 90 and avg < 85):
 print("Grade A")
 print("CGPA : 8")

elif(avg >= 80):
 print("Grade A-")
 print("CGPA : 7")

elif(avg > 75):
 print("Grade B+")
 print("CGPA : 6")
 
elif(avg > 70):
 print("Grade B")
 print("CGPA : 5")

elif(avg < 70 and avg >65):
 print("Grade B-")
 print("CGPA : 4")

elif(avg < 65 and avg >60):
 print("Grade C+")
 print("CGPA : 3")
 
elif(avg < 60 and avg >55):
 print("Grade C")
 print("CGPA : 2")

elif(avg < 55 and avg >50):
 print("Grade C-")
 print("CGPA : 1")
 
else:
 print("Positive Integer.!")