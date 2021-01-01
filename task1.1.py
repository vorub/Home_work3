def my_func(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'error', 'Ошибка числа'
    except ZeroDivisionError:
        return 'Вы ввели 0, на 0 делить нельзя'
    return answer
num_1 = float(input('Введите число 1: '))
num_2 = float(input('Введите число 2: '))
print(my_func(num_1, num_2))