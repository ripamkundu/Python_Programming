def Sort_Tuple(tup): 
    lst = len(tup) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 
            if (tup[j][1] > tup[j + 1][1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup 
tup =[('Ripam', 17), ('Parthib', 10), ('Sneha', 28),
('Arijit', 5), ('kuhali', 20), ('Debomita', 15), ('Sabarna', 19)]      
print(Sort_Tuple(tup)) 