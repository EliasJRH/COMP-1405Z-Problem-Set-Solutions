
content = None
content_list = None


def load(fname):
    global content # chaning the global values
    global content_list
    content = open(fname).read() #reads the list, sets it to content
    content_list = content.split() # puts all the items into an interable list
    content.close()

def commonword(list_to_compare):
    global content_list # referencing the global content list
    word_freq = {} # creating dictionary
    for word in list_to_compare:
        for word2 in content_list:
            if word2 == word:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
    most_freq = max(word_freq, key=word_freq.get, default=None)
    return most_freq
        
def commonpair(word):
    global content_list
    word_freq = {}
    for item in range(len(content_list)-1):
        if content_list[item] == word:
            if content_list[item + 1] not in word_freq:
                word_freq[content_list[item + 1]] = 0
            word_freq[content_list[item + 1]] += 1
    return max(word_freq, key=word_freq.get, default=None)
    
def countall():
    global content_list
    return len(content_list)

def countunique():
    global content_list
    unique_words = {}
    for word in content_list:
        if word not in unique_words:
            unique_words[word] = True
    return len(unique_words)


load('testfile1.txt')
print(commonword(['banana','car','pear']))
print(commonpair('banana'))
print(countall())
print(countunique())