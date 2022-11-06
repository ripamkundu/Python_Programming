print("Enter the month and year to get the specific Number of days : ")
month =  int(input("Enter the Month : "))
if month in(1, 3, 5, 7, 8, 10, 12):
 day = 31
 print("Number of Days is : ", (month, day))
elif month in(4, 6, 9, 11):
 day =  30
 print("Number of Days : ",(month, day))
elif month == 2:
 year = int(input("Enter the year : "))
 if (year % 4 == 0) and (not (year % 100 == 0)\ or (year % 400 == 0)) :
  day = 29
 else:
  day = 28
 print("Number of days : ", (month,  year, day))
else:
 print("Invalid Choice..!")
