list1 = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
def flatten_list(list1):
    list2 = []
    for row in list1:
        for number in row:
            list2.append(number)
    list2.sort()        
    return list2
print(flatten_list(list1))    
    
