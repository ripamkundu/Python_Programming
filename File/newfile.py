a = input("Enter File some contain : ")
f = open('user.txt', 'w')
f.write(a)
f.close()

f = open('user.txt', 'r')
print(f.read())

f = open('user.txt', 'r')
data = f.read().replace(" ", " ")   #read the content of file and replace spaces with nothing
number = len(data)                  #get the length of the data
print("Number of character in text file : ", number)