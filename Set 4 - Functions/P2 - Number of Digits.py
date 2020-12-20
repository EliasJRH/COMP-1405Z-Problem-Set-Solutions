print('Number of Digits')

def numDigits(num): # takes a string as an arguement
    num = str(num) # converts string to integer value
    count = 0 # variable to hold the count of digits
    for x in num: # for every character in the num string
        count += 1 # increase count by 1
    return count # return the count

print(numDigits(14324324243243325650))