#Sort Words in Alphabetic Order

string = input("Enter a value of Alphabetic Character: ")
w = [word.lower() for word in string.split()]
w.sort()
print("The sorted words are :")
for word in w:
   print(word)