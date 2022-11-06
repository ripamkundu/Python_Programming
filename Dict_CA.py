dict_list = {'Ripam' : 14, 'PHP' : 12, 'Python' : 5}
  
print("The original dictionary : " + str(dict_list))
new = dict(reversed(list(dict_list.items())))
  
print("New dictionary : " + str(new))