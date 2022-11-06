n=int(input("Enter the number of terms: "))
s=0
for i in range(1,n+1):
 s = s + (1/i)
print("The sum of series is : ",round(s,2))