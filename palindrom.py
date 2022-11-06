n = int(input( "Enter a number : "))
t = n
r = 0
while ( n > 0 ):
 d = n%10
 r = r*10+d
 n = n//10
if (t==r):
 print( " The number is palindrom ! " )
else:
 print ( "The number is not palindrom ! " ) 