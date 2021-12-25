def max2(a, b):
    if a > b:
        return a 
    elif a < b:
        return b
    else:
        return "equal"
a = int(input("a = "))
b = int(input("b = "))
print(max2(a, b))

