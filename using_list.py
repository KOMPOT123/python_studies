a = ['apple', 'mango', 'cat', 'banans']

print ('i must', len(a), 'dam')

print('buys: ', end=' ')
for item in a:
    print(item, end=' ')

print('\nAnd need this')
a.append('rice')
print('now my list: ', a)

print('start sort')
a.sort()
print('sort end: ', a)

print('first: ', a[0])
olditem = a[0]
del a[0]
print('izi', olditem)
print('now list', a)
print(a[0])
