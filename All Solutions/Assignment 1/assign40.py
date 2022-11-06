#copy file

import copy
source = "\E:\Python Programming\Python Assignment.txt"
destination = "\E:\Python Programming\python"

try:
	copy.copyfile(source, destination)
	print("File copied successfully.")

except copy.SameFileError:
	print("Source and destination represents the same file.")

except IsADirectoryError:
	print("Destination is a directory.")

except PermissionError:
	print("Permission denied.")

except:
	print("Error occurred while copying file.")

