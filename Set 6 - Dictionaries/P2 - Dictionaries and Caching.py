import time


def factorial(num):
    fac = 1
    for x in range(num, 0,-1):
        fac *= x
    return fac

def cachedfactorial(num, facs):
    fac = 1
    for x in range(num, 0, -1):
        if x in facs:
            fac *= facs[x]
            facs[num] = fac 
            return fac
        else:
            fac *= x
    facs[num] = fac
    return fac

facs = {1:1,
2:2}
command = ""
while command != 'q':
    command = input('Enter a command: ')
    if command == 'fac':
        innum = int(input('Enter a number: '))
        starttime = time.time()
        print(factorial(innum))
        print(f'Total time: {time.time() - starttime}')
    elif command == 'cfac':
        innum = int(input('Enter a number: '))
        starttime = time.time()
        cachedfactorial(innum, facs)
        print(facs)
        print(f'Total time: {time.time() - starttime}')
