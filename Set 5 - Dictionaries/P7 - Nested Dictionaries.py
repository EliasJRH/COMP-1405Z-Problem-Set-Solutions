print("Nested Dictionaries")

dic = {}

def addword(dic, stri):
    last_char = ""
    temp_dic = None
    for char in range(len(stri)):
        if char == 0:
            if stri[char] not in dic:
                dic[stri[char]] = {}
            last_char = stri[char]
            temp_dic = dic[last_char]
        else:
            if stri[char] not in temp_dic:
                temp_dic[stri[char]] = {}
            last_char = stri[char]
            temp_dic = temp_dic[last_char]
    temp_dic['.'] = 1
            
def addword_recursive(dic, stri):
    print(stri)
    if stri[0] not in dic:
        dic[stri[0]] = {}
    temp_dic = dic[stri[0]]
    stri = stri[1:]
    if len(stri) == 0:
        temp_dic['.'] = 1
        return
    return addword_recursive(temp_dic, stri)
            
def checkword(dic, stri):
    last_char = ""
    temp_dic = None
    for char in range(len(stri)):
        if char == 0:
            if stri[char] not in dic:
                return False
            last_char = stri[char]
            temp_dic = dic[last_char]
        else:
            if stri[char] not in temp_dic:
                return False
            last_char = stri[char]
            temp_dic = temp_dic[last_char]
    if '.' in temp_dic:
        return True
    else:
        return False

def initialize(dic, filename):
    with open(filename) as infile:
        for line in infile:
            word = line.strip()
            print(word)
            addword_recursive(dic, word)

addword_recursive(dic, "been")
print(checkword(dic, "been"))
initialize(dic, 'words.txt')
print(dic)


