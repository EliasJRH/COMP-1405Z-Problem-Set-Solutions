print('Top X')

num_list = [8, 3, 1, 2, 9, 4, 5, 7, 6]

def topx(list1, index):
    minimum = None
    new_list = []
    for x in list1:
        if len(new_list) < index:
            new_list.append(x)
        else:
            for y in new_list:
                if minimum == None or y < minimum:
                    minimum = y
            if x > minimum:
                new_list.remove(minimum)
                new_list.append(x)
            minimum = None
    return new_list
    
print(topx(num_list, 4))