import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

if guess == 'heads':
    guess = 1
else:
    guess = 0

toss = random.randint(0, 1)

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')