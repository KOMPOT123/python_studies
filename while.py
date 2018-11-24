number = 23
running = True

while running:
    guess = int(input('number'))
    
    if guess == number:
        print('yes')
    elif guess < number:
        print('x>{0}'.format(guess))
    else:
        print('x<{0}'.format(guess))
else:
    print('end')
print('easy')
