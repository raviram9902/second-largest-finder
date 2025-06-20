def secondlargest(list_1,):
    max_1= 0
    secondmax = 0
    for i in list_1:
        if i>max_1:
            secondmax= max_1
            max_1= i
            
        elif i>secondmax and i!=max_1:
            secondmax=i
    print(secondmax)
        
secondlargest([2,33,18,2819,0,1263,2817])        