def Count(str):
	upper, lower, number, character, word, leng, delet_space, special = 0, 0, 0, 0, 0, 0, 0, 0
	for i in range(len(str)):
		if str[i].isupper():
			upper += 1
		elif str[i].islower():
			lower += 1
		elif str[i].isdigit():
			number += 1
		elif str[i].ischaracter():
		    character += 1
        elif str[i].isword():
		    word += 1
        elif str[i].islen():
			leng += 1
        elif str[i].isdelete_space():
			delete_space += 1
        else:
			special += 1
	print('Upper case letters:', upper)
	print('Lower case letters:', lower)
	print('Number:', number)
	print('Character:', character)
	print('Word:', word)
	print('Length:', leng)
	print('Delete_Space:', delete_space)
	print('Special characters:', special)

str = int(input("enter your thought: "))
Count(str)