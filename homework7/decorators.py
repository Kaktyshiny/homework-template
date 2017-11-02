
def cancel(func):
    return IndexError('{} is canceled!'.format(func.__name__))


def count_execution(func):
    pass


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)
