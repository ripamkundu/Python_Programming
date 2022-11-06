nums = []
n = int(input("How many Number You want ?"))
print("Enter Elements of List: ")
for i in range(0,n):
    val=int(input())
    nums.append(val)
print("List IS : ", n)
x = int(input("Enter seaching elemnt in the list: "))
try :
 pos = nums.index(x)
 print("\nThe Searing list is : ", pos)
except ValueError as e:
 print(e)

