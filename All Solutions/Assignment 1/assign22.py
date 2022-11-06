#Check Whether a String is Palindrome or Not

print ("Enter a number : ")
n = int (input())
t = n
r = 0

while(n<0):
 d = n%10
 r = r*10+d
 n = n//10
if (t == n):
 print ("It is a palindrome Number")
else:
 print ("It is not a palindrome Number")