str = input("Enter Some contain : ")
f = {}
for char in str:
    if char in f:
        f[char] +=1
    else:
        f[char] = 1
count = max(f, key = f.get)
print("Maximum Character is : ",count)
print("It is repeted %d times " %(f[count]))