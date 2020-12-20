print('Trip Distance Calculator')
import math
first_city = [0,0]
second_city = [0,0]
choice = ""
distance = 0.0
first_city[0] = int(input('Enter x coordinate of first city: '))
first_city[1] = int(input('Enter y coordinate of first city: '))
while choice != 'q':
    second_city[0] = int(input('Enter x coordinate of next city: '))
    second_city[1] = int(input('Enter y coordinate of next city: '))
    distance += float(math.sqrt(((first_city[0] - second_city[0]) ** 2) + ((first_city[1] - second_city[1]) ** 2)))
    first_city[0] = second_city[0]
    first_city[1] = second_city[1]
    choice = input('''Would you like to keep calculating distances?
Enter q to quit
Enter anything else to continue: ''')
print('Total distance travelled was ' + str(distance))