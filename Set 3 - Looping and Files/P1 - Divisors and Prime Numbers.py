print('Divisors and Prime Numbers')
num = input('Enter a number: ')
while not num.isdigit():
    print('Invalid input')
    num = input('Enter a number: ')
num = int(num)
x = 1
sumN = 0
print('The divisors are: ')
while x <= (num / 2):
    if (num % x == 0):
        print(x)
        sumN += x
    x += 1
print(num)
sumN += num
print('The sum of the divisors is ' + str(sumN))
if (sumN == (num + 1)):
    print('The number is prime')
else:
    print('The number is not prime')

