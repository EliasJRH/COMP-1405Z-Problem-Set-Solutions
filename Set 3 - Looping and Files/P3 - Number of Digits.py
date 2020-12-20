print('Number of Digits')
user_choice = input('Enter an integer: ')
total = 0 
while not user_choice.isdigit():
    print('Invalid input')
    user_choice = input('Enter an integer: ')
for x in user_choice:
    total += 1
print('There are ' + str(total) + ' digits in that number.')