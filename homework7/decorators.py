
def cancel(func):
    def cancel_func():
        return IndexError('{} is canceled!'.format(func.__name__))

    return cancel_func()


def count_execution(func):
    def gen_count():
        count = 0
        while True:
            yield count
            count += 1

    def wrapper():
        gen = gen_count()
        return next(gen)

    return wrapper


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)
