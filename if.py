number = 23
guess = int(input('Input number: '))

if guess == number:
    print('yes')
elif guess < number:
    print('x>{0}'.format(guess))
else:
    print('x<{0}'.format(guess))
print('easy')
