import listmaker

print('Galloping Search')

def galloping_search(list, value):
    if len(list) == 1 and list[0] == value:
        return 0
    elif (len(list) == 1 and list[0] != value) or len(list) == 0:
        return None
    last_index = 1
    first_index = 0
    while last_index < len(list) and list[last_index] < value:
        first_index = last_index
        last_index *= 2
    return binarysearch(list,value,first_index,last_index)

def binarysearch(list, item, spoint, epoint):
    start = spoint
    end = epoint
    mid = 0
    searches = 0
    while start <= end:
        mid = int((start + end)/2)
        miditem = list[mid]
        if miditem == item:
            return mid
        elif miditem < item:
            start = mid + 1
        elif miditem > item:
            end = mid - 1
        searches += 1
    return None

print(galloping_search(listmaker.create_sorted_list(100), 18))