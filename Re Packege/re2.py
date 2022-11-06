import re
st = ("Light,  Height, fight, Good, Sound")
st2= re.findall("ight*", st)
print(st2)