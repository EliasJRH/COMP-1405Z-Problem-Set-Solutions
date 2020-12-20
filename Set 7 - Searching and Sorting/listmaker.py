import random

def create_sorted_list(range_of_nums):
    numslist = []
    for x in range(range_of_nums):
        if random.randint(0,100) > 75:
            numslist.append(x)
    return numslist
    
    
def create_unsorted_list(length, maxval):
    numslist = []
    for x in range(length):
        numslist.append(random.randint(0,maxval))
    return numslist
    
def create_unique_list(length, maxval):
    numslist = []
    for x in range(length):
        numslist.append(random.randint(0,maxval))
    return numslist
    
def create_2d_list(length, maxval):
    numslist = []
    templist = []
    for x in range(length):
        numslist.append([])
        for y in range(2):
            numslist[x].append(random.randint(0, maxval))
    return numslist
 
print(create_unsorted_list(20, 80))