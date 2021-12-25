a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
c1 = int(input("c1 = "))
d1 = int(input("d1 = "))
e1 = int(input("e1 = "))
a2 = int(input("a2 = "))
b2 = int(input("b2 = "))

list1 = [a1, b1, c1, d1, e1]
list2 = [a2, b2]

def filter_list(list1, list2):
    list3 = []
    for number in list1:
        if number not in list2:
            list3.append(number)
    return list3

print(filter_list(list1, list2))

