arr = []
print("Enter two lists of students")
name = input("Enter Student name: ")
num = eval(input("Enter Marks : "))

for i in range(len(name)):
    arr.append(name[i] + num[i])
print("Student List :")
print(arr)