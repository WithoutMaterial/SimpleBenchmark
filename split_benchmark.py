"""
    данный код не претендует на точность бенчмарка, написан чисто в целях написать какую-нибудь реализационную задачку
    сложнее hello_world.py, используя модули стандартной библиотеки.
"""

import random
import time

SPACE = " "
NEWLINE = "\n"
EMPTY = ""


def timer(func):
    def timed_func(test):
        start_time = time.time()
        func(test)
        log(f"Время исполнения: {time.time() - start_time} секунд.")
    return timed_func


@timer
def split(test):
    return test.split()


@timer
def my_split(test):
    result = []
    for c in test:
        if c != SPACE:
            if result:
                result[-1] += c
            else:
                result += c
        else:
            if result and result[-1] != EMPTY:
                result += EMPTY
    if result[-1] == EMPTY:
        result.pop()
    return result


def checker(first, second):
    if first != second:
        raise ResultError(first, second)
    log("Тест успешно пройдён")


class ResultError(Exception):

    def __init__(self, *results):
        self.results = results

    def __str__(self):
        return f"Результаты не совпали: {NEWLINE.join(f'{index}: {res}' for index, res in enumerate(self.results))}"


def make_test(size, alphabet, spaces=True):
    if spaces:
        alphabet.append(SPACE)
    return str([random.choice(alphabet) for _ in range(size)])


def log(message, error=False):
    if error:
        print("Ошибка, подробнее:", message)
    else:
        print(message)


if __name__ == '__main__':

    # 10 ^ 5 длина теста, алфавит (он ни на что не влияет, чисто для усложнения реализации) из одной буквы
    test_size = 10 ** 5
    test_alphabet = ['a']
    current = make_test(test_size, test_alphabet)
    try:
        checker(split(current), my_split(current))
    except ResultError as e:
        log(e, error=True)
    
    """
        Вывод:
            Время исполнения: 0.005604743957519531 секунд.
            Время исполнения: 1.2181675434112549 секунд.
            Тест успешно пройдён
    """
