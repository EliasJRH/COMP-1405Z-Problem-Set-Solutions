import random
num_to_guess = random.randint(1,100)
player_guess = input('Guess the number from 1 to 100: ')
while (not player_guess.isdigit()):
    print('Input an integer')
    player_guess = input('Guess the number from 1 to 100: ')
player_guess = int(player_guess)
if (player_guess == num_to_guess):
    print('You got it!')
elif (player_guess < num_to_guess):
    print('''You didn't get it 
You were under by ''' + str(num_to_guess - player_guess) + '''
The number was ''' + str(num_to_guess))
else:
    print('''You didn't get it 
You were over by ''' + str(player_guess - num_to_guess)+ '''
The number was ''' + str(num_to_guess))