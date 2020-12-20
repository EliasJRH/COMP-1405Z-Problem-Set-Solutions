CADRates = {'CAD': 1.00, 'USD': 0.76, 'GPB': 0.59, 'EUR': 0.64, 'JPY': 79.13, 'BTC': 0.000069, 'DOGE': 271.963704}
starting_rate = input('''Select starting rate from list of rates below
CAD
USD
GPB
EUR
JPY
BTC
DOGE
''')
starting_rate = starting_rate.upper()
while (starting_rate not in CADRates):
    print('Rate not found')
    starting_rate = input('''Select starting rate from list of rates below
CAD
USD
GPB
EUR
JPY
BTC
DOGE
''')
    starting_rate = starting_rate.upper()
converting_rate = input('''Select rate to convert to from list of rates below
CAD
USD
GPB
EUR
JPY
BTC
DOGE
''')
converting_rate = converting_rate.upper()
while converting_rate not in CADRates:
    print('Rate not found')
    converting_rate = input('''Select rate to convert to from list of rates below
CAD
USD
GPB
EUR
JPY
BTC
DOGE
''')
    converting_rate = converting_rate.upper()
amount = float(input('How much cash do you want to conver? '))
print(str(amount) + ' ' + starting_rate + ' = ' + str(((amount / CADRates[starting_rate]) * CADRates[converting_rate])) + ' ' + converting_rate)