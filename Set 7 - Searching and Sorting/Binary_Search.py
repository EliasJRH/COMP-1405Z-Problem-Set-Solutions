def binarysearch(list, item):
    start = 0
    end = len(list) - 1
    mid = 0
    searches = 0
    while start <= end:
        mid = int((start + end)/2)
        miditem = list[mid]
        print(miditem)
        if miditem == item:
            print(f'Searches performed: {searches}')
            return mid
        elif miditem < item:
            start = mid + 1
        elif miditem > item:
            end = mid - 1
        searches += 1
    return -1
    
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binarysearch(list1, 4))