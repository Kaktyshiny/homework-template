from functools import reduce


def modulo_five():
    list_of_num = [1, 4, 5, 30, 99]
    def remainder(num):
        return num % 5
    result = list(map(remainder, list_of_num))
    return result


def to_string():
    item = [3, 4, 90, -2]
    def make_string(string):
        return str(string)
    result = list(map(make_string, item))
    return result


def filter_string():
    list_of_item = ['some', 1, 'v', 40, '3a', str]

    def is_string(items):
        return not isinstance(items, str)

    no_strings = list(filter(is_string, list_of_item))
    return no_strings


def count_letters():
    list_of_word = ['some', 'other', 'value']
    sum_all = len(reduce(lambda word, word2: word + word2, list_of_word))
    return sum_all
