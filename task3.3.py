def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'
num_1 = float(input('Введите число 1: '))
num_2 = float(input('Введите число 2: '))
num_3 = float(input('Введите число 2: '))
print(my_func(num_1, num_2, num_3))