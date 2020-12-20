print('Increasing Integers')
number = 0
streak = 0
longest_streak = 0
integer = ""
check = False
while (integer != 'q'):
    while check == False:
        try:
            integer = input('Enter an integer: ')
            if integer == 'q':
                break
            integer = int(integer)
            check = True
        except ValueError:
            print('Not an integer')
    check = False        
    if integer == 'q':
        break
    elif integer > number:
        number = integer
        streak += 1
    else:
        if streak > longest_streak:
            longest_streak = streak
        streak = 1
        number = integer
if streak > longest_streak:
    longest_streak = streak
print('Length of longest increasing sequence is: ' + str(longest_streak))