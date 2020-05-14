
def add(*args):
    """args ЭТО НАЗВАНИЕ ПЕРЕМЕННОЙ
    ОНО МОЖЕТ БЫТЬ ДРУГИМ .
    УПАКОВЫВАЕТ ВСЕ ПЕРЕМЕННЫЕ
    ТАК МОЖНО БУДЕТ ПЕРЕДОВАТЬ ЛЮБОЕ
    КОЛИЧЕСТВО ПЕРЕМЕННЫХ
    args = arguiments = аргумент
    """
    print(args)
    print(sum(args))

# add(3,5,5)
l = [1,2,3,4]
# add(*l)
'''
можно передовать список
в качестве аргумента
но нелзя давать еще один аргумен
рядом с args пример add(a,*args)
это будет работать но криво
и не стоит использовать генераторы yield
оно попросту сожрет дофига памяти
'''

def add_l(*args, **kwargs):
    '''
    **kwargs работает как args но если *args
    переобразует в кортеж
    то **kwargs в словарь
    kwargs здесь может быть любым другим аргументом
    а ** упаковывает в словарь
    а * упаковывает в кортеж
    '''
    print(args)
    print(kwargs)

s =[2,4,5,6]

# add_l(l, street='lenina', house=12)


jack = {
    'name': 'jack',
    'car': 'bmw'
}

john = {
    'name': 'john',
    'car': 'audi'
}
saken = {
    'car': 'lexus'
}

users = [jack, john, saken]# это список словарей

cars = [person['car'] for person in users]
# print(cars)

# cars = []
# for person in users:
#     cars.append(person['car'])
#
# print(cars)

names = [person.get('name', '') for person in users]
"""
если использовать метод get он заменяет элемент если его нету
так что у нас не будеть исключении при вызова car где нет имени
а выведет пустую строку это хорошая практика
"""
print(names)

#=------------------------------------Фильтрация-----------------------------

nameses = ['jack','john','oleg','saken']

new_names = [n for n in names if n.startswith('j')]
print(new_names)

# new_names = []
# for n in nameses:
#     if n.startswith('j'):
#         new_names.append(n)
# print(new_names)
