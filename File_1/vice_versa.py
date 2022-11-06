str=input("enter your thought: ")
new_str=str
for a in str:
  if(a.isupper())== True:
    new_str+=(a.lower())
  elif(a.islower())==True:
    new_str+=(a.upper())
print("new_str")    