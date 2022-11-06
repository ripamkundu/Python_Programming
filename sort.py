arr=[]
n=int(input("How Many Number You Want ?"))
print("Enter Your " + str(n) + " Number : ")
for k in range(n):
    d=int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))

for i in range(0,len(arr)-1):
    for j in range(i+1, len(arr)):
         if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
print("sorted List is : ")
print(arr)   
    
