n = int(input("Enter a Number : "))
l = [i for i in range(1, n+1)]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Odd Number : ",odd)
print("Even Number : ",even)