def my_func(x, y):
    try:
        answer = x ** y
    except TypeError:
        return 'Enter float'
    return answer
x = float(input('Введите положительное число 1: '))
y = float(input('Введите отрицательное число 2: '))
print(my_func(x, y))