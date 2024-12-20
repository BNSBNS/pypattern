from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f'total time = {after - before}')
        return rv
    return f


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f'running {f.__name__}')
                rv = f(*args,**kwargs)
                print(f'rv {rv}')
            print('---returning')
            return rv
        return wrapper
    return inner

# @timer
@ntimes(2)
def add(x,y = 10):
    return x + y

@timer 
def sub(x,y=10):
    return x- y



print(f'add 10 {add(10)}')

print(f'sub {sub(10)}')