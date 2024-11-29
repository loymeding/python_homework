'''
Создайте функцию, которая будет открывать файл, считывать его содержимое и выводить на экран только те строки,
которые содержат числовые значения. Если файл не найден, должно возникнуть исключение FileNotFoundError,
если внутри файла попалось значение отличное от числа, должно возникнуть исключение TypeError.
Файл должен иметь текстовый формат.
'''


def read_numeric_lines_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        number = float(line)
                        print(f"Строка {line} успешно считана")
                    except ValueError:
                        raise TypeError(f"Недопустимое значение в строке: '{line}'")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


read_numeric_lines_from_file('data.txt')

