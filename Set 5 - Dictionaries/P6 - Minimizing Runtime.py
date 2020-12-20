import random
import time

def addend(list, dict, value):
    list.append(value)
    if value not in dict:
        dict[value] = 0
    dict[value] += 1
	
def removestart(list, dict):
    if len(list) == 0:
        return None
    if dict[list[0]] > 0:
        dict[list[0]] -= 1
    return list.pop(0)
	
def containslinear(list, value):
	return value in list

def containshash(dict, value):
    if value in dict and dict[value] >= 1 :
        return True
    else:
        return False

list = []
hash = {}
addprob = 100
removeprob = 90
repeat = 50000
maxval = 500
searchlist = []
#randomly build the data by probabilistically adding/removing items to the list
#also generate a list of items to search for later
#also make sure that the dictionary search is returning the same result as the list search
for i in range(repeat):
	if random.randint(0,100) < addprob:
		addend(list, hash, random.randint(0,maxval))
	if random.randint(0,100) < removeprob:
		removestart(list, hash)
		
	searchlist.append(random.randint(0,maxval))
	
	searchnum = random.randint(0,maxval)
	
	if containslinear(list, searchnum) != containshash(hash, searchnum):
		print("Error: dictionary and list search returned different results")
		exit()

start = time.time()
for i in searchlist:
	containslinear(list, i)
end = time.time()
print("Linear time: ", (end-start))

start = time.time()
for i in searchlist:
	containshash(hash, i)
end = time.time()
print("Hash time: ", (end-start))
