
def cancel(func):
    def cancel_func():
        return '{} is canceled!'.format(func.__name__)

    return ''


def count_execution(func):
    def gen_count():
        count = 0
        while True:
            yield count
            count += 1


    gen = gen_count()
    print(next(gen))

    return func(*args, **kwargs)


def catch(func):
    try:
        print(func(*args, **kwargs))
    except Exception as e:
        print(e)
