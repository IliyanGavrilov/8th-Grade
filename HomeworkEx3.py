def ones_to_text(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'

def teens_to_text(num):
    if num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'

def tens_to_text(num):
    if (num // 10) % 10 == 2:
        return 'twenty'
    elif (num // 10) % 10 == 3:
        return 'thirty'
    elif (num // 10) % 10 == 4:
        return 'fourty'
    elif (num // 10) % 10 == 5:
        return 'fifty'
    elif (num // 10) % 10 == 6:
        return 'sixty'
    elif (num // 10) % 10 == 7:
        return 'seventy'
    elif (num // 10) % 10 == 8:
        return 'eighty'
    elif (num // 10) % 10 == 9:
        return 'ninety'

def hundreds_to_text(num):
    if num // 100 == 0:
        return ""
    elif num // 100 == 1:
        return 'one hundred'
    elif num // 100 == 2:
        return 'two hundred'
    elif num // 100 == 3:
        return 'three hundred'
    elif num // 100 == 4:
        return 'four hundred'
    elif num // 100 == 5:
        return 'five hundred'
    elif num // 100 == 6:
        return 'six hundred'
    elif num // 100 == 7:
        return 'seven hundred'
    elif num // 100 == 8:
        return 'eight hundred'
    elif num // 100 == 9:
        return 'nine hundred'

def number_to_text(num):
    print(hundreds_to_text(num), end="")
    
    if (num // 10) % 10 == 1:
        if num // 100 != 0:
            print(" and ", end="")
        print(teens_to_text(num % 100), end="")
    elif (num // 10) % 10 == 0:
        if num % 10 != 0 and num // 100 != 0:
            print(" and", ones_to_text(num % 10), end=" ")
    else:
        if num // 100 != 0:
            print(" and ", end="")
        print(tens_to_text(num), end=" ")
        
    if (num // 10) % 10 != 1:
        if num % 10 == 0:
            if (num // 10) % 10 == 0 and num // 100 == 0:
                print("zero")
        else:
            if num // 100 == 0 or (num // 10) % 10 != 0:
                print(ones_to_text(num % 10))
        
num = int(input("Choose a number = "))
number_to_text(num)
