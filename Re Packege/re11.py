import re
  st = "7477638690 pin code : 700031"
  pattern = re.compile (r,'\d\d\d\d\d\d\d\d\d\d')
  st = re.search (pattern, st)
  print(st)
