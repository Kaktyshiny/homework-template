import random
from datetime import datetime, timedelta


def all_even_numbers():
    for i in range(0,100,2):
        yield i


def random_increasing_number(start_from = 0):
    last_num = start_from
    next_num = random.randint(last_num, last_num + 100)
    while True:
        next_num = random.randint(next_num, next_num+100)
        yield next_num


def next_day():
    i = 0
    today = datetime.today().day

    while True:
        yield today + timedelta(days=i).days
        i += 1
