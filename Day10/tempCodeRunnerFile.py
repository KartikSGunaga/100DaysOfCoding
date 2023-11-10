def isLeap(year):
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    else:
        return False

year = int(input("enter the year: ")) 
month = int(input("enter the month: "))

match month:
    case 1:
        print(31)
        break
    case 2:
        if(isLeap(year)):
            print(29)
        else:
            print(28)
        break
    case 3:
        print(31)
        break
    case 4:
        print(30)
        break
    case 5:
        print(31)
        break
    case 6:
        print(30)
        break
    case 7:
        print(31)
        break
    case 8:
        print(31)
        break
    case 9:
        print(30)
        break
    case 10:
        print(31)
        break
    case 11:
        print(30)
        break
    case 12:
        print(31)
        break