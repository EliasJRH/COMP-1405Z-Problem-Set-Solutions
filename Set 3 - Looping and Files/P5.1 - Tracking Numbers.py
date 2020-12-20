print('Tracking numbers')
largest, smallest, average, total, positive, negative = 0,0,0,0,0,0
file = open(input('Enter file name: '))
with file as file:
    for line in file:
        if total == 0:
            largest = int(line)
            smallest = int(line)
        else:
            if int(line) > largest:
                largest = int(line)
            elif int(line) < smallest:
                smallest = int(line)
        average += int(line)
        total += 1
        if int(line) > 0:
            positive += 1
        elif int(line) < 0:
            negative += 1
print('---------------------------------')
print('Largest number: ' + str(largest))
print('Smallest number: ' + str(smallest))
print('Average: ' + str(average/total))
print('Number of positives: ' + str(positive))
print('Number of negatives: ' + str(negative))
print('---------------------------------')
