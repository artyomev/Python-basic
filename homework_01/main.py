"""
Домашнее задание №1
Функции и структуры данных
"""
import math as m


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, int(m.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def filter_numbers(nums_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    callbacks = {
        'odd': lambda x: x % 2,
        'even': lambda x: not x % 2,
        'prime': is_prime
    }
    return list(filter(callbacks[filter_type], nums_list))
