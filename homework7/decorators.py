import sys

def cancel(func):
    def cancel_func():
        return IndexError('{} is canceled!'.format(func.__name__))

    return func


def count_execution(func):
    func.count = 0

    def _gen_count(*args, **kwargs):
        func.count += 1

        print('Count is', func.count)

        return func(*args, **kwargs)

    return _gen_count


def catch(func):
    try:
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    except Exception as e:
        print(e)

print(sys.getsizeof(''))
