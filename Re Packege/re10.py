import re
st = ("ripamkundu636gmail.com")
st2= re.findall("\w", st)  # small Latter
st3= re.findall("\W", st)   # capital  Latter
print(st2)
print(st3)
  