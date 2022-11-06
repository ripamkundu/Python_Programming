#Hash File

import hashlib

python = 65536 #64kb in binary 
sha1 = hashlib.sha1()
with open('assign15.py', 'rb') as f:
while True:
 data = f.read(python)
   if not data:
      break
   sha1.update(data)
print("SHA1: {0}".format(sha1.hexdigest()))