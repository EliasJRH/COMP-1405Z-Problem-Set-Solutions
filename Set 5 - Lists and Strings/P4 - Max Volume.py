print('Largest Volume')

def maxvolume(list_of_volumes):
    volume = 1
    current_max = None
    for x in list_of_volumes:
        for index in x:
            volume *= index
        if current_max == None or volume > current_max:
            current_max = volume
        volume = 1
    return current_max

test_list = [[1,2,3],[32,65,2],[21,34,7]]
print(maxvolume(test_list))    