a = input("Enter File some contain : ")
f = open('user.txt', 'w')
f.write(a)
f.close()

f = open('user.txt', 'r')
print(f.read())

f = open('user.txt', 'r')
data = f.read()           #get the length of the data
number = len(data)
print("Number of character in text file : ", number)