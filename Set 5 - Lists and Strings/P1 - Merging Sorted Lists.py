print('Merge Sorted Lists')
list1 = [1,3,5]
list2 = [2,4,6,7,8]

def mergeSortedLists(list_1, list_2):
    p1 = 0
    p2 = 0
    first_reached = False
    second_reached = False
    new_list = []
    while first_reached == False and second_reached == False:
        if list_1[p1] <= list2[p2]:
            new_list.append(list_1[p1])
            p1 += 1
        elif list_1[p1] > list2[p2]:
            new_list.append(list_2[p2])
            p2 += 1
        if p1 == len(list_1):
            first_reached = True
        elif p2 == len(list_2):
            second_reached = True
    if first_reached:
        for x in range(p2, len(list_2)):
            new_list.append(list_2[x])
    elif second_reached:
        for x in range(p1, len(list_1)):
            new_list.append(list_1[x])
    return new_list

    
 
print(mergeSortedLists(list1,list2))