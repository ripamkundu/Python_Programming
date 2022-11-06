n = int(input("Enter a Number : "))
l = [i for i in range(1, n+1)]
print(l)
odd=[]
even=[]
for i in range(len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
print("Odd Number : ",odd)
print("Even Number : ",even)
