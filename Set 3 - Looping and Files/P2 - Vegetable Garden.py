print('Vegetable Garden')
print('Enter True or False for application, enter anything else to exit')
answer = input('It rained today? ')
days_without_rain = 0
while answer == 'True' or answer == 'False':
    if answer == 'False':
        days_without_rain += 1
    elif answer == 'True':
        days_without_rain = 0
    if days_without_rain == 3:
        print('Quick! Water your garden before all the plants die and you starve to death!')
        days_without_rain = 0
    answer = input('It rained today? ')