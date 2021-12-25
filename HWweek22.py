""" Задача 1 """

def rook_can_capture(x, y):
    if x[0] == y[0] or x[1] == y[1]:
        return True
    else:
        return False

""" Задача 2 """

def filter_by_digit_length(a, b):
    result = []
    for i in a:
        if len(str(i)) == b:
            result.append(i)

    return result

""" Задача 3 """

def test_jackpot(a):
    first = a[0]
    for i in a:
        if i != first:
            return False

    return True

""" Задача 4 """

def sub_reddit(x):
    result = x.split("/")
    return result[4]
    

""" Задача 5 """

def percent_to_decimal(a):
    a = a[:-1]
    return float(a) / 100



    


