import listmaker

def count(list, value):
    return findend(list, value) - findstart(list,value) + 1
    

def findstart(list,value):
    start = 0
    end = len(list) - 1
    mid = 0
    point = None
    while start <= end:
        mid = int((start + end)/2)
        midval = list[mid]
        if midval == value and list[mid - 1] != value:
            point = mid
            break
        elif (midval == value and list[mid - 1] == value) or  midval > value:
            end = mid - 1
        elif midval < value:
            start = mid + 1  
    return point

def findend(list,value):
    start = 0
    end = len(list) - 1
    mid = 0
    while start <= end:
        mid = int((start + end)/2)
        midval = list[mid]
        if midval == value and list[mid + 1] != value:
            point = mid
            break
        elif (midval == value and list[mid + 1] == value) or  midval < value:
            start = mid + 1 
        elif midval > value:
            end = mid - 1
    return point
    

x = listmaker.create_unique_list(20, 5)
x.sort()
print(x)
print(count(x, 2))
