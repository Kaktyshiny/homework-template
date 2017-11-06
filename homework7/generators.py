import random
from datetime import datetime, timedelta


def all_even_numbers():
    for i in range(0,100,2):
        yield i


def random_increasing_number(start_from = 0):
    next_num = random.randint(start_from, start_from + 100)
    while True:
        next_num = random.randint(next_num, next_num+100)
        yield next_num


def next_day():
    day = datetime.today().date()

    while True:
        yield day
        day += timedelta(days=1)
