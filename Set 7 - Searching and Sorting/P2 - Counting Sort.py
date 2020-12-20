import listmaker

print('Counting Sort')

def countsort(list):
    unique = {}
    sorted_list = []
    for x in list:
        if x not in unique:
            unique[x] = 0
        unique[x] += 1
    unique_list = sorted(unique)
    for num in unique_list:
        for value in range(unique[num]):
            sorted_list.append(num)
    print(sorted_list)
    
countsort(listmaker.create_unique_list(20, 5))