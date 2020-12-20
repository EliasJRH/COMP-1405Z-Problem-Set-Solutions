import datetime
print('Hi Welcome to Buy-Nary Computing Electrons store!')
pcs, laptops, tablets, toasters = 0,0,0,0
bill = 0
shopping, check = True, False
choice = input('''Select which product you'd like to purchase
1. Desktop Computer ($850 each)
2. Laptop Computer ($1225 each)
3. Tablet ($600 each)
4. Toaster Oven ($85 each)
5. Enter 'q' to quit
''')
if choice == 'q':
    print('Thank you for visiting Buy-Nary Computing Electronics!')
else:
    while shopping:
        if choice == 'q':
            shopping = False    
        elif not choice.isdigit() and choice != 'q':
            print('Sorry we don\'t seem to support that choice')
        elif int(choice) < 1 or int(choice) > 4:
            print('Sorry we don\'t seem to support that choice')
        else:
            choice = int(choice)
            while check == False:
                try:
                    quantity = input('How much would you like to buy? ')
                    quantity = int(quantity)
                    check = True
                except ValueError:
                    print('Invalid Input')
            check = False
            if (choice == 1):
                print('Desktop Computers ($850 each)')
                pcs += quantity
                bill += (850 * quantity)
            elif (choice == 2):
                print('Laptop Computer ($1225 each)')
                laptops += quantity
                bill += (1225 * quantity)
            elif (choice == 3):
                print('Tablet ($600 each)')
                tablets += quantity
                bill += (600 * quantity)
            elif (choice == 4):
                print('Toaster Oven ($85 each)')
                toasters += quantity
                bill += (85 * quantity)
            quantity = ""
            
        if shopping == False:
            print('Thank you for shopping with us!')
            if pcs > 0 or laptops > 0 or tablets > 0 or toasters > 0:
                print('Here is your receipt')
                print('''-----------------------------------------------------------
|                Buy-Nary Computing Electronics         |
|                    Assistant: Elias Hawa                      |
|             ''' + str(datetime.datetime.now()) + '''               |
|                                                                            |''')
                if pcs > 0:
                    print('|    Desktop Computer(s) / ' + str(pcs) + ' * $850  = $' + str(pcs * 850) + '    |') 
                if laptops > 0:
                    print('|    Laptop(s) / ' + str(laptops) + ' * $1225  = $' + str(laptops * 1225) + '                     |') 
                if tablets > 0:
                    print('|    Tablet(s) / ' + str(tablets) + ' * $600  = $' + str(tablets * 600) + '                        |') 
                if toasters > 0:
                    print('|    Toaster Oven(s) / ' + str(toasters) + ' * $85  = $' + str(toasters * 85) + '                |') 
                print('''|                                                                            |
|                                                                            |
|                                                                            |
|       Thank you for shopping with us today!       |
-----------------------------------------------------------''')
        else:
            choice = input('''Select which product you'd like to purchase
1. Desktop Computer ($850 each)
2. Laptop Computer ($1225 each)
3. Tablet ($600 each)
4. Toaster Oven ($85 each)
5. Enter 'q' to quit
''')
        
        
