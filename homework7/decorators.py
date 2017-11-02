
def cancel(func):
    def cancel_func():
        return '{} is canceled!'.format(func.__name__)

    return cancel_func()


def count_execution(func):
    def gen_count():
        count = 0
        while True:
            yield count
            count += 1


    gen = gen_count()
    print(next(gen))

    return func()


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)
