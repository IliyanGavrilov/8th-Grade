def split_change(a):
    if a // 5 > 0:
        print(a // 5, "* 5") 
        a = a % 5
    if a // 2 > 0:
        print(a // 2, "* 2")
        a = a % 2
    if a // 1 > 0:
        print(a // 1, "* 1")
        
a = int(input("Change = "))
split_change(a)
