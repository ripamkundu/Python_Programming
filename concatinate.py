def concatenate_list(list):
    list =input ("enter your thought: ")
    result= ' '
    for element in list:
        result += str(element)
    return result

print(concatenate_list(list))