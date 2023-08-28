import random

top_of_number = input('Type a number: ')
if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number <= 0:
        print('Please type a number above 0 next time')
        quit()
else:
    print('Please type a number next time')
    quit()

random_number = random.randint(0,top_of_number) #random [0;top_of_number]
guesses = 0

while True:
    guesses += 1
    user_guess = input('Guess a number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Guess a number next time')
        quit()

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess >= random_number:
        print('You were above random number')
    else:
        print('You were below random number')

print('You got it in', guesses, 'guesses')
