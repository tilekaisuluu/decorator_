def myDecorator(func):
    def wrapper_func(a, b=1, *args, **kwargs):
        print('Calling {0} {1}'.format(func.__name__, (a, b, args, kwargs)))
        func(a, b, *args, **kwargs)
        print('Finished {0}({1})'.format(func.__name__, (a + b)))
        # return func(a, b, *args, **kwargs)
    return wrapper_func


@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    print('kwargs:', kwargs)
    return a + b



testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)
print()
