try:
    text = input('enter something --->  ')
except EOFError:
    print('Why do you do to me EOF?')
except KeyboardInterrupt:
    print('you do esc.')
else:
    print('You enter {0}'.format(text))
