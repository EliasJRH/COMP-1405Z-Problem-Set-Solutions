
def error_check(low,high,inputted,weight):
    while (inputted < low or inputted > high):
        inputted = int(input('Inputted value is invalid, input again: ')) * weight

midterm1 = int(input('Enter first midterm mark: ')) * 0.2
error_check(0,100,midterm1,0.2)
midterm2 = int(input('Enter second midterm mark: ')) * 0.2
error_check(0,100,midterm2,0.2)
midterm3 = int(input('Enter third midterm mark: ')) * 0.2
error_check(0,100,midterm3,0.2)
final = int(input('Enter final exam mark: '))
error_check(0,100,final,1)
bonus = int(input('Enter bonus question mark (out of ten): '))
error_check(0,10,bonus,1)
print('Final mark is: ' + str(midterm1 + midterm2 + midterm3 + (final * (0.4 - (bonus/100))) + bonus)+ '%')
