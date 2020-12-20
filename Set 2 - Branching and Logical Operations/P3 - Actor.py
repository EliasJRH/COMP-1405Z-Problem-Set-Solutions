print('The actor being considered is Ryan Reynolds')
print('The possible movies are: Deadpool, Green Lantern, Detective Pikachu, 6 Underground')
question_one = input('Is his character a superhero? ')
if question_one == 'Yes':
    question_two = input('Is the movie good? ')
    if question_two == 'Yes':
        print('The movie is Deadpool')
    else:
        print('The movie is Green Lantern')
else:
    question_two = input('Does his character use a gun? ')
    if question_two == 'Yes':
        print('The movie is 6 Underground')
    else:
        print('The movie is Detective Pikachu')