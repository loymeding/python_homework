'''
Изучите модуль itertools в Python. Напишите программу, которая использует этот модуль для решения следующих задач:

Создание бесконечного генератора чисел.
Применение функций к каждому элементу в итераторе.
Объединение нескольких итераторов в один.
Используйте функции и методы из модуля itertools, чтобы выполнить указанные задачи. Убедитесь, что ваш скрипт может обрабатывать исключения, связанные с отсутствием данных в итераторах.
'''


import itertools


# Создание бесконечного генератора чисел
def infinite_numbers():
    for number in itertools.count(start=1):
        yield number


# Применение функции к каждому элементу в итераторе
def apply_function(iterator, function):
    try:
        return map(function, iterator)
    except Exception as e:
        print(f"Ошибка при применении функции: {e}")
        return iter([])  # Возвращаем пустой итератор в случае ошибки


# Объединение нескольких итераторов в один
def merge_iterators(*iterators):
    try:
        return itertools.chain(*iterators)
    except Exception as e:
        print(f"Ошибка при объединении итераторов: {e}")
        return iter([])


if __name__ == "__main__":
    # Бесконечный генератор чисел
    infinite_gen = infinite_numbers()

    # Применяем функцию к первым 10 элементам
    doubled_numbers = apply_function(itertools.islice(infinite_gen, 10), lambda x: x * 2)

    print("Удвоенные числа:")
    for num in doubled_numbers:
        print(num)

    # Пример объединения итераторов
    first_iter = [1, 2, 3]
    second_iter = [4, 5, 6]

    merged = merge_iterators(first_iter, second_iter)

    print("Объединённые числа:")
    for num in merged:
        print(num)

