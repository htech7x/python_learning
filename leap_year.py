# ver.1

def is_leap(year):
    leap = False
    
    if year % 4 != 0:
        leap = False
    elif year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True

    return leap

year = int(input())
print(is_leap(year))


# ver.2

def leap_year(year):
    if year % 4 != 0:
        print("Simple year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("Leap year !!!")
        else:
            print("Simple year")
    else:
        print("Simple year")
