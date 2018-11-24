print('Простое присваивание1')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist

del shoplist[0]

print('shoplist: ', shoplist)
print('mylist', mylist)

print('копирование при помощи полной вырезки')
mylist = shoplist[:]
del mylist[0]

print('shoplist', shoplist)
print('mylist', mylist)
