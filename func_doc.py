def printMax(x, y):
    '''Выводит максимальное из двух чисел

       Оба значения должны быть целыми числами.'''
    x = int(x)#конвертирует в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'bigest')
    else:
        print(y, 'bigest')

printMax(input(), input())
print(printMax.__doc__)
