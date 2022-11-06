import re
st = ("Light,  Height, nigght, fight, Good, Sound")
st2= re.findall("o{2}", st)
print(st2)
