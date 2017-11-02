
def cancel(func):
    def cancel_func():
        return IndexError('{} is canceled!'.format(func.__name__))

    return cancel_func()


def count_execution(func):
    # def wrapper():
    #     wrapper.count += 1
    #     print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
    #
    # wrapper.count = 0
    # return wrapper
    import time

    def wrappers():
        t = time.clock()
        return func.__name__, time.clock() - t
        yield wrappers

    def wrapper():
        wrapper.called += 1
        return func()

    wrapper.called = 0
    wrapper.__name__ = func.__name__
    return wrapper


def catch(func):
    try:
        func()
    except Exception as e:
        print(e)
