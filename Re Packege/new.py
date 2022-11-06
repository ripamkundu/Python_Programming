import regex as re
list = ("Ripam, Pritam, Baban, Joydeep, Priyanka")
st = re.findall("deep*", list)
print(st)