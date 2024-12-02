from module.calculator import Calculator


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = Calculator.sum_of_list(numbers)
print(f"Сумма чисел равна: {result}.")
