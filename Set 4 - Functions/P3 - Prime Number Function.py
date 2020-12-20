import math
print('Prime Number Function')


def isPrime(num): # takes in an integer as an argument
    prime = True # prime value set to True that will return when the for loop is finished if it's not stopped before
    if num % 2 == 0: # if the number is 0, the program returns false
        return False
    for x in range(2,math.ceil(num/2)): # otherwise, a for loop starts until the ceiling value of the number divided by 2
        if num % x == 0: # if the number divided by x returns a division with remained 0
            prime = False # sets prime to false
            return prime # returns prime as false
    return prime # if the loop finished and a multiple was not found, prime is returned as true

for x in range (1,101): # checks all numbers from 1 to 100 if they're 100
    print(isPrime(x))