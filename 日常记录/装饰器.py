def func(fn):
    def wrapper(*args, **kwargs):
        print(1111)
        return fn(*args, **kwargs)
    return wrapper


@func  # test = func(test)
def test(num):
    print(num)


test(222)

