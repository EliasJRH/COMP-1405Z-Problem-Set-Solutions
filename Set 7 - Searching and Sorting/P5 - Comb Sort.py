import listmaker
import math

print('Comb Sort')

def combsort(list):
    gap = len(list)
    shrink = 1.3
    sorted = False
    
    while sorted == False:
        gap = int(gap/shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(list):
            if distance(list[i]) > distance(list[i + gap]):
                list[i], list[i + gap] = list[i + gap], list[i]
                sorted = False
            i += 1
    return list
    
def distance(points):
    return math.sqrt((math.pow(points[0], 2)) + math.pow(points[1], 2))
    
print (combsort([[5, 3], [1, 1], [1, 4], [3, 5], [1, 1], [2, 5], [4, 2], [5, 4], [0, 1], [3, 1]]))
# print()
# [[5, 3], [1, 1], [1, 4], [3, 5], [1, 1], [2, 5], [4, 2], [5, 4], [0, 1], [3, 1]]