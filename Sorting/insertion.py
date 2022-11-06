arr=[]
n=int(input("How Many Number You Want ?"))
print("Enter Your " + str(n) + " Integers : ")
for k in range(n):
    d=int(input())
    arr.append(d)
print("Unsorted Array Is : " +str(arr))

for i in range(1,len(arr)):
    j = arr[i]
    pos = i
    while(j < arr[pos-1] and pos > 0):
        temp = arr[pos]
        arr[pos] = arr[pos-1]
        arr[pos-1] = temp
print("Sorted Array Is : " +str(arr))

