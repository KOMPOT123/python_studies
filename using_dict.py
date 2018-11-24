ab = {'Swaroop' : 'ebana hyuna',
      'Larry'   : 'larry hyu',
      'Mats'    : 'hyu too',
      'Spam'    : 'syka'
}
print('Swaroop', ab['Swaroop'])

del ab['Spam']
print('\n nol blua\n' .format(len(ab)))

for name, address in ab.items():
    print('{0} s adres {1}' .format(name, address))
ab['Gui'] = 'hyulo'

if 'Gui' in ab:
    print('\nGui', ab['Gui'])
