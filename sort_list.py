def Sorting(lst):
	lst.sort(key=len)
	return lst
lst = [520,49,3,999]
print(Sorting(lst))
