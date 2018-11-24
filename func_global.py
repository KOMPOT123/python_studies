x = 50
def func():
    global x

    print('x =', x)
    x = 2
    print('now x =', x)
func()
print('x in central block =', x)
