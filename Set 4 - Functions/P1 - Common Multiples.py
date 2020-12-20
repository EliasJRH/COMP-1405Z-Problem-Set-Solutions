print('Common Multiples')

def ismultiple(num_a, num_b):# Takes two numbers as arguement
    if num_b % num_a == 0: # if num_b divided by num_a returns a number with a remainer of 0
        return True # return true
    else:
        return False # otherwise return false

def commonmultiple(num_a, num_b, num_c): # takes three numbers as arguement
    if ismultiple(num_c, num_a) and ismultiple(num_c, num_b):
        # if num c is a multiple of both num_a and num_b
        return True # return true
    else:
        return False# otherwise return false
        
num_1 = int(input('Enter first number: ')) # gets first integer input
num_2 = int(input('Enter second number: '))# gets second integer input

for x in range(1, 101): # checks for all numbers from 1 to 100 that are common multiples of both num_1 and num_2
    if commonmultiple(num_1, num_2, x):
        print(x) # prints the numbers out if it returns true