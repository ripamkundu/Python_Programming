import re
st = ("Light,  Height, nighht, fight, Good, Sound")
st2= re.findall("ight{2}", st)
print(st2)