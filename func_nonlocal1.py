def func_other():
    x = 2
    print('x =', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('local x change', x)

func_other()
