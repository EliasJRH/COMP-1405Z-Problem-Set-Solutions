largest, smallest, average, total, positive, negative = 0,0,0,0,0,0
num = input('Enter an integer: ')
if num == 'q':
    print('Largest number: ' + str(largest))
    print('Smallest number: ' + str(smallest))
    print('Average: ' + str(average))
    print('Number of positives: ' + str(positive))
    print('Number of negatives: ' + str(negative))
else:
    while not num.isdigit():
        print('Invalid input')
        num = input('Enter an integer: ')
    while num != 'q':
        if num != 'q':
            num = int(num)
            total += 1
            if total == 1:
                largest = num
                smallest = num
            else:
                if num > largest:
                    largest = num
                elif num < smallest:
                    smallest = num
            average += num
            if num > 0:
                positive += 1
            elif num < 0:
                negative += 1
        print('Number registered')
        num = input('Enter an integer: ')
        while not num.isdigit() and num != 'q':
            print('Invalid input')
            num = input('Enter an integer: ')
        
if total > 0:
    print('---------------------------------')
    print('Largest number: ' + str(largest))
    print('Smallest number: ' + str(smallest))
    print('Average: ' + str(average/total))
    print('Number of positives: ' + str(positive))
    print('Number of negatives: ' + str(negative))
