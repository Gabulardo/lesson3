def my_func(arg1, arg2):
    if arg2 != 0:
        return arg1 / arg2
    else:
        print('Знаменатель не может быть равен 0')

arg1 = int(input('Введите числитель: '))
arg2 = int(input('Введите знаменатель: '))
result = my_func(arg1, arg2)
print(result)
