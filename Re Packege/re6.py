import re
st = ("Light,  Height, nigght, fight, Good, Sound")
st2= re.findall("ig{2}", st)
print(st2)
