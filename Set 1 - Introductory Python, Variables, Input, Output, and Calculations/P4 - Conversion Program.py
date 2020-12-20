choice = input('''(1)Convert from C --> F
(2)Convert from F --> C
''')
if (choice == '1'):
    celcius = input('Enter degrees in Celcius: ')
    print(celcius + '° Celcius is ' + str((int(celcius) * 1.8) + 32) + '° Farenheit')
else:
    farenheit = input('Enter degrees in Farenheit: ')
    print(farenheit + '° Farenheit is ' + str(((int(farenheit) - 32) / 1.8)) + '° Farenheit')