hidden_name= 'carol'
guess_count = 0
guess_limit= 3
while guess_count < guess_limit:
    guess = (input('Guess: '))
    guess_count += 1
    if guess == hidden_name:
        print('You Won')
        break
else:
    print('Sorry incorrect')