def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'numbers seems'
    else:
        return y

print(maximum(input('number A = '), input('number B = ')))
print(max(input('number A = '), input('number B = ')))
