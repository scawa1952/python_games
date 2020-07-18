# This is a Gues the Number Game
import random

guessesTaken = 0

print('Hello.  What is your name?')
myName = input()

number = random.randint(1, 20)
print('Number is ' + str(number))
gotIt = False
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high!')
    elif guess == number:
        print('Your guess is just right!  Cool beans!')
        gotIt = True
        break



if gotIt == True:
    print('It took you ' + str(guessesTaken) + ' guesses to get it.')
else:
    print('Too bad.  My number was ' + number + '.')








