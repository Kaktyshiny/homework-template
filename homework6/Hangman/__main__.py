import json
import os
import random

from Hangman.hangman_image import hangman_image

# Закидываем в словарь слова
with open('Hangman/words.json', 'r', encoding='utf-8') as fh:
    dictionary = json.load(fh)['words']


class Game(object):
    def __init__(self, word):
        self.word = word
        self.len = len(word)
        self.previous = []
        self.solving = str('_' * self.len)
        self.stage = 0
        self.rights = 0

    def __str__(self):
        # Возвращает загаданное слово в нужном нам формате
        right_format = ''
        for i in self.solving:
            right_format += i + ' '
        return right_format

    def print_image(self):
        return hangman_image[self.stage]

    def is_right_letter(self, letter):
        flag = False
        for i in range(self.len):
            if self.word[i] == letter:
                self.solving = self.solving[:i] + letter + self.solving[i + 1:]
                flag = True
                self.rights += 1
        if flag:
            return True
        return False

    def is_english_word(self):
        # Вовзвращает True, если слово на английском
        for i in self.word:
            if not is_english_letter(i):
                return False
        return True

    def is_previous_letter(self, letter):
        # Возвращает была ли уже названа данная буква ранее
        if letter in self.previous:
            return True
        return False

    def is_game_over(self):
        # Возвращает -1 - если проиграл, 1 - если выиграл
        # False - если игра не окончена
        if self.stage >= 6:
            return -1
        if self.word == self.solving:
            return 1
        return False


def is_english_letter(letter):
    '''
    Проверяем, что буква английская
    :param letter: буква
    :return: True - если маленькая английская
    '''
    if letter >= 'a' and letter <= 'z':
        return True
    return False


def game_logic(current_game):
    '''
    Запускает игру с заданным словом
    :param word: загаданное слово в виде объекта класса game
    :return: True - если выиграл, False - если проиграл
    '''
    print('\n\rИгра начинается!\n\r', current_game.print_image())

    while not current_game.is_game_over():
        print('\n\rЗагаданное слово:', current_game)
        current_letter = input(' Введите букву: ')

        if len(current_letter) != 1:
            print('Введите только 1 букву!')
            continue
        if current_game.is_previous_letter(current_letter):
            print('Такая буква уже была, попробуйте другую!')
            continue
        while not is_english_letter(current_letter):
            current_letter = input('Ошибка: Буква должна быть из английского '
                                   'алфавита!\n\r Введите букву: ')
        current_game.previous.append(current_letter)
        print('Вы уже вводили следующие буквы:', current_game.previous)

        if not current_game.is_right_letter(current_letter):
            print('Такой буквы нет!')
            current_game.stage += 1
            print(current_game.print_image())

    if current_game.is_game_over() == -1:
        print('\r\nВы проиграли! Загаданное слово:', current_game.word)
        print('\r\nВы угадали', current_game.rights, 'букв(ы) за ',
              len(current_game.previous), 'попыток')
        return False
    if current_game.is_game_over() == 1:
        print('\n\rЗагаданное слово:', current_game.word)
        print('\r\nВы выиграли!')
        print('\r\nВы угадали', current_game.rights, 'букв(ы) за ',
              len(current_game.previous), 'попыток')
        return True


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    clear_console()
    print('Добро пожаловать!')

    while True:
        try:
            type_of_game = int(input('\n\rВыберите с кем играть:'
                                     '\n\r 1. С компьютером'
                                     '\n\r 2. С человеком'
                                     '\n\r 3. Выйти'
                                     '\n\rВаш ответ: '))
            if type_of_game == 1:
                current_game_number = 0
                current_wins_your = 0
                current_wins_comp = 0
                current_stats = 0
                current_stats_rights = 0

                while current_wins_your < 2 and current_wins_comp < 2:
                    word = Game(random.choice(dictionary))
                    if game_logic(word):
                        current_wins_your += 1
                    else:
                        current_wins_comp += 1

                    current_stats_rights += word.rights
                    current_stats += len(word.previous)
                    current_game_number += 1

                    print('По итогам предыдуших игр ваша статистика:\n\r'
                          '    Угаданных букв:', current_stats_rights, '\n\r'
                          '    Количество попыток:', current_stats)

                if current_wins_your == 2:
                    print('Вы смогли обыграть компьютер! Поздравляем!')
                else:
                    print('Вы проиграли компьютеру!')

                print('Вы сыграли', current_game_number, 'игры')

            elif type_of_game == 2:
                current_wins_one = 0
                current_wins_two = 0
                current_game_number = 0
                current_stats_one = 0
                current_stats_rights_one = 0
                current_stats_two = 0
                current_stats_rights_two = 0

                while current_wins_one < 2 and current_wins_two < 2:
                    current_player = int(current_game_number) % 2 + 1
                    word = Game(input('Игрок №{} загадывает слово: '.format(
                        current_player)).lower())
                    if not word.is_english_word():
                        print('Ошибка: Слово должно быть '
                              'на английском языке')
                        continue
                    if len(word.word) == 0:
                        continue
                    clear_console()
                    another_player = (int(current_game_number) + 1) % 2 + 1
                    print('Игрок №', current_player,
                          ' загадал вам слово.\n\r Игрок №',
                          another_player, 'отгадывает слово.')

                    if game_logic(word):
                        if current_player == 1:
                            current_wins_two += 1
                        else:
                            current_wins_one += 1

                    else:
                        if current_player == 1:
                            current_wins_one += 1
                        else:
                            current_wins_two += 1

                    if current_player == 1:
                        current_stats_one += len(word.previous)
                        current_stats_rights_one += word.rights
                    else:
                        current_stats_two += len(word.previous)
                        current_stats_rights_two += word.rights

                    print('\n\rПо итогам предыдуших игр статистика '
                          'первого игрока:\n\r    Угаданных букв:',
                          current_stats_rights_one,
                          '\n\r    Количество попыток:',
                          current_stats_one)
                    print('\n\rПо итогам предыдуших игр статистика второго '
                          'игрока:\n\r    Угаданных букв:',
                          current_stats_rights_two,
                          '\n\r    Количество попыток:',
                          current_stats_two)

                    current_game_number += 1
                    print('Текущий счет:', current_wins_one,
                          ':', current_wins_two)

                if current_wins_one == 2:
                    print('\n\r\n\rПервый игрок победил!')
                else:
                    print('Второй игрок победил!')

                print('\n\r\n\rВы сыграли', current_game_number, 'игры')

            elif type_of_game == 3:
                raise KeyboardInterrupt
            else:
                raise IndexError
        except IndexError:
            print('Ошибка: Вводить можно только числа 1, 2 или 3')
        except ValueError:
            print('Ошибка: Вводить можно только числа!')


if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('\n\rДо встречи! Возвращайся ещё! :)')
