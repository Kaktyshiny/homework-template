
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

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper



def catch(func):
    try:
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    except Exception as e:
        print(e)

@catch
def normal(text):
    raise ValueError(text)

print(normal('k'))
