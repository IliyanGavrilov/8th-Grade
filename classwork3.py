def max3(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif a < b:
        if b > c:
            return b
        else:
            return c
    else:
        if a < c:
            return c
        else:
            return a
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(max3(a, b, c))
