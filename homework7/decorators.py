
def cancel(func):
    def cancel_func():
        return '{} is canceled!'.format(func.__name__)
    
    return cancel_func()


def count_execution(func):
    def wrapper():
        wrapper.count += 1
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))

    wrapper.count = 0
    return wrapper


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)
