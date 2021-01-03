
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print({my_func((input('Введите имя: ')),
       input('Введите фамилию: '),
       input('Введите год рождения: '),
       input('Введите город проживания: '),
       input('Введите адрес электронной почты: '),
       input('Введите номер телефона: '))})




