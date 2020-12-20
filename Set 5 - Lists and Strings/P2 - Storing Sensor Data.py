print('Storing Sensor Data')

measurements = [2,7,1,11,14,3,6,2,1,8]
max_length = 10

def measure(num):
    count = 0
    for x in measurements:
        count += 1
    if count == max_length:
        del measurements[0]
        measurements.append(num)
    else:
        measurements.append(num)

def average():
    count = 0
    total = 0
    for x in measurements:
        count += 1
        total += x
    return (total/count)
    
def min():
    first = True
    minimum = None
    for x in measurements:
        if first:
            minimum = x
            first = False
        else:
            if x < minimum:
                minimum = x
    return minimum

def max():
    first = True
    maximum = None
    for x in measurements:
        if first:
            maximum = x
            first = False
        else:
            if x > maximum:
                maximum = x
    return maximum
    
def isdanger():
    danger_zone = 3
    maximum = None
    minimum = None
    for x in range(danger_zone):
        if maximum == None:
            maximum = measurements[len(measurements) - (x + 1)]
            minimum = measurements[len(measurements) - (x + 1)]
        else:
            if measurements[len(measurements) - (x + 1)] > maximum:
                maximum = measurements[len(measurements) - (x + 1)]
            elif measurements[len(measurements) - (x + 1)] < minimum:
                minimum = measurements[len(measurements) - (x + 1)]
    if ((maximum - minimum) > 10):
        return True
    else:
        return False

measure(7)
print(measurements)
print(average())
print(min())
print(max())
print(isdanger())