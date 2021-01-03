# def my_func(x, y):
#     return x ** abs(y)
# print(my_func(float(input('Введите действительное положительное число: ')),
#       int(input('Введите целое отрицательное число: '))))

def my_func(x, y):
    for i in range(abs(y - 1)):
        x *= x
        return x
print(my_func(float(input('Введите действительное положительное число: ')),
                  int(input('Введите целое отрицательное число: '))))

