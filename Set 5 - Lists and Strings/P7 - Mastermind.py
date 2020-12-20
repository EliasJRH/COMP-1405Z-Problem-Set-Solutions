import random
print('Mastermind')

def generate_list():
    game_list = []
    for x in range(5):
        game_list.append(random.randint(0,9))
    return game_list

def start_game(passcode):
    print('I\' set my password, enter 5 digits in the range of [0-9] separated by spaces')
    for x in range(10,0,-1):
        correct_guesses = 0
        guess = input(f'{x} guesses remaining >').split()
        for y in range(len(guess)):
            guess[y] = int(guess[y])
            if (guess[y] == passcode[y]):
                correct_guesses += 1
        if correct_guesses == 5:
            print('What? You figured it out?! No! How were you able to solve my unsolveable puzzle?!')
            break
        else:
            print(f'{correct_guesses} of 5 correct')
    print(f'Hah! Looks like you couldn\' figure out that my secret password was {passcode}!... Wait a second...')
    
    
start_game(generate_list())

