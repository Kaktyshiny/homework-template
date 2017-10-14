# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x', ]
    for i in range(0, 1000):
        # Делаем 1000 рандомных шагов, чтобы помешать поле
        move = random.choice(list(MOVES.keys()))
        field_status = perform_move(field, move)
        if field_status is True:
            field = field_status
    return(field)

    # Если делать через функйию random.shuffle:
    #
    # random.shuffle(field)
    # return(field)


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    line = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            line[j] = field[i * 4 + j]
        print(line)


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x', ]:
        return(True)
    else:
        return(False)


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    key = MOVES[key]
    for i in range(len(field)):
        if field[i] == EMPTY_MARK:
            index = i
    if (index + key >= 0) and (index + key < 16):
        if (key == 1 or key == -1) and \
                (((index + key) % 4 == 0) and ((index % 4 == 3))) or \
                (((index + key) % 4 == 3) and ((index % 4 == 0))):
            return(field)
        else:
            field[index], field[index + key] = field[index + key], field[index]
            return(field)
    else:
        return(False)


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    move = ''
    while move not in MOVES:
        move = input('Ходить клавишами W, A, S и D! Повторите ваш ход:')
    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    print('Добро пожаловать в уникальную игру! Итааак... мы начинаем!')
    print('Мы перемешали поле и сейчас оно выведется вам на экран!')
    current_field = shuffle_field()
    print('Знаком x обозначена пустая клетка')
    print_field(current_field)
    while not(is_game_finished(current_field)):
        user_moving = handle_user_input()
        field_status = perform_move(current_field, user_moving)
        if field_status is False:
            print('Вы не можете так походить!')
        else:
            current_field = field_status
            print_field(current_field)
    print('Поздравляем! ВЫ ВЫИГРАЛИ СУПЕР ИГРУ')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('shutting down')
