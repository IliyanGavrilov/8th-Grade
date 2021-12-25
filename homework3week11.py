n = int(input("n = "))
def pascal_triangle(n):
    list1 = [[1]]
    for i in range(n-1):
        list2 = []
        for j in range(i+2):
            if j == 0 or j == i+1:
                list2.append(1)
            else:
                list2.append(list1[i][j] + list1[i][j-1])
        list1.append(list2)

    for row in list1:
        print(' ' * (n-len(row)), end="")
        for i in row:
            print(i, end=" ")
        print()
          
    
pascal_triangle(n)

