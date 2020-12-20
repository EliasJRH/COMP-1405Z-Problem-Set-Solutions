print('Largest Number')
list_of_nums = [2,5,765,23,5,78,23,84,2,5,3,54]

def maxvalue(list_to_read):
    largest = None
    for x in list_to_read:
        if largest == None or x > largest:
            largest = x
    return largest
    
print(maxvalue(list_of_nums))