print('Binary Quiz Game')

def pow2(num): # takes in an integer as an arguement
    last_square = 0 # integer to hold the value of the last square
    for x in range(num + 1): # for every number up until the input number + 1
        if 2 ** x > num: # if x squared is greater 
            return last_square
        else:
            last_square = 2 ** x

print(pow2(0))