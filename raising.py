class ShortInputException(Exception):
    '''my class except'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('enter something         ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('eof ne pokazhetsa')
except ShortInputException as ex:
    print('ShortInputException: длина стороки - - {0};\
    ожидалось как минимум {1}'.format(ex.length, ex.atleast))
else:
    print('не было исключений')
