#Calculator Program
import time
import threading

choice = input('''(A)ddition
(S)ubtraction
(M)ultiplication
(D)ivison
''')

def vaporize(name):
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    print('Finding target...')
    sleep(1)
    print('Vaporizing...')
    sleep(1)
    print('Target: ' + name + ' successfully vaporized')
    

if choice == 'A':
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2))
elif choice == 'S':
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    print(str(num1) + ' - ' + str(num2) + ' = ' + str(num1 - num2))
elif choice == 'M':
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    print(str(num1) + ' x ' + str(num2) + ' = ' + str(num1 * num2))
elif choice == 'D':
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    print(str(num1) + ' / ' + str(num2) + ' = ' + str(num1 / num2))
elif choice == 'Vaporize':
    target_name = input('Select target: ')
    x = threading.Thread(target=vaporize, args=(target_name,))
    x.start()
else:
    print('This function is not supported')
    


    
        
        
        
        
        