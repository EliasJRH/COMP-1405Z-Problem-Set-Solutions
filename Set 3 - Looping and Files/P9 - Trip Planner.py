import os
import math
print('Trip Planner')
check = False
choice = ""
while choice != 5:
    while check == False:
        choice = input('''1) Enter a new city
2) Remove a city
3) List cities
4) Plan a trip
5) Quit
''')
        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                print('Invalid Input')
            else:
                check = True
        except ValueError:
            print('Invalid Input')
    check = False
    if choice == 1:
        city_name = input('Enter City Name: ')
        while check == False:
            x_coord = input('Enter x coordinate of City: ')
            try:
                x_coord = int(x_coord)
                check = True
            except ValueError:
                print('Invalid Input')
        check = False
        while check == False:
            y_coord = input('Enter y coordinate of City: ')
            try:
                y_coord = int(y_coord)
                check = True
            except ValueError:
                print('Invalid Input')
        check = False
        print('City added to city database')
        cities = open('cities.txt', "a")
        cities.write(city_name + ' ' + str(x_coord) + ' ' + str(y_coord) + "\n")
        cities.close()
    elif choice == 2:
        print('------------CITIES------------')
        cities_read = open('cities.txt', "r")
        with cities_read as file:
            for line in file:
                words = line.split()
                for entry in range(len(words)):
                    if entry == 0:
                        print(words[entry] + ': (', end="")
                    elif entry == 1:
                        print(words[entry] + ',', end="")
                    elif entry == 2:
                        print(words[entry] + ')')
        print('--------------------------------')
        city_to_remove = input('Which city would you like to remove? ')
        city_to_remove = city_to_remove.lower()
        cities_read = open('cities.txt', "r")
        cities_write = open('newfile.txt', "w")
        with cities_read as input_file:
            with cities_write as output:
                for line in input_file:
                    word = line.split()
                    if word[0].lower() != city_to_remove:
                        output.write(line)
        os.remove('cities.txt')
        os.rename('newfile.txt', 'cities.txt')
        print('City removed')
    elif choice == 3:
        print('------------CITIES------------')
        cities_read = open('cities.txt', "r")
        with cities_read as file:
            for line in file:
                words = line.split()
                for entry in range(len(words)):
                    if entry == 0:
                        print(words[entry] + ': (', end="")
                    elif entry == 1:
                        print(words[entry] + ',', end="")
                    elif entry == 2:
                        print(words[entry] + ')')
        print('--------------------------------')
    elif choice == 4:
        print('Enter q to quit at anytime')
        cities_list = []
        distance = 0
        first_city_coords = [0,0]
        second_city_coords = [0,0]
        second_city = ""
        cities_read = open('cities.txt', "r")
        with cities_read as file:
            for line in file:
                word = line.split()
                cities_list.append(word[0].lower())
        print('------------CITIES------------')
        cities_read = open('cities.txt', "r")
        with cities_read as file:
            for line in file:
                words = line.split()
                for entry in range(len(words)):
                    if entry == 0:
                        print(words[entry] + ': (', end="")
                    elif entry == 1:
                        print(words[entry] + ',', end="")
                    elif entry == 2:
                        print(words[entry] + ')')
        print('--------------------------------')
        first_city = input('Enter name of first city: ')
        if first_city != 'q':
            while first_city not in cities_list:
                print('Invalid City Name')
                first_city = input('Enter name of first city: ') 
            first_city = first_city.lower()
            cities_read = open('cities.txt', "r")
            with cities_read as file:
                for line in file:
                    word = line.split()
                    if word[0].lower() == first_city:
                        first_city_coords[0] = int(word[1])
                        first_city_coords[1] = int(word[2])
                        break
            while second_city != 'q':
                second_city = input('Enter name of next city: ')
                if second_city != 'q':
                    while second_city not in cities_list:
                        print('Invalid City Name')
                        first_city = input('Enter name of next city: ')
                    cities_read = open('cities.txt', "r")
                    with cities_read as file:
                        for line in file:
                            word = line.split()
                            if word[0].lower() == second_city:
                                second_city_coords[0] = int(word[1])
                                second_city_coords[1] = int(word[2])
                    distance += float(math.sqrt(((first_city_coords[0] - second_city_coords[0]) ** 2) + ((first_city_coords[1] - second_city_coords[1]) ** 2)))
                    first_city_coords[0] = second_city_coords[0]
                    first_city_coords[1] = second_city_coords[1]
                else:
                    print('Total distance is ' + str(distance))   