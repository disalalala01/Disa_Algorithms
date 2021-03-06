a = [['astana', 495], ['almaty', 500], ['shymkent', 555]]

r = dict(astana=495, almaty=500, shymkent=555)

t = dict(a)

q = dict.fromkeys(['a', 'b', 'c'], 100)# Преврашяет каждый элемент в ключ второй элемент в значение каждого

b = {}
v = dict()# Пустой словарь

#----------------------------------------------------------------------------------
"""
Ключем может быть строка и число
а значением может быть любой тип
Но ключем не может быть изменяемый тип объекта
Обрашение пройсходит по ключю словаря
"""
d = {
    1: 'one',
    'hello': 'two',
    3: [1, 2 , 3]
}
d[4] = 'four'# Добавляем новый ключ со значением
d[3] = 'Три' # Меняем значение ключа

#-----------------------------------------------------------------------------------------

person = {}
s="SAKENOV Saken Astana ENU 5 4 5 5 4 3 5"
s = s.split()
person['Surename'] = s[0]
person['Name'] = s[1]
person['city'] = s[2]
person['univer'] = s[3]
person['marks'] = []

for i in s[4:]:
    person['marks'].append(int(i))

del person['city']#  Удаление Элемента

print('marks' in person, 'Saken' in person, 5 not in person)# Есть ли то или иной ключ в словаре
f = len(person)

if 5 in person:
    print(person[5])
else:
    person[5] = 'five'

# for key in person:
#     print(key, person[key])

#-------------------------------------------------------------------------------------------------------


"""
Методы словаря
"""
h = {
    1: 'one',
    2: 'two',
    3: 'three'
}
def clear_all(x:dict):
    x.clear()# Метод очистки словаря

print(h.get(4, 'che tam'))# Метод get() получает значение по ключю Если ключа нет может вернуть второй параметер

h.setdefault(7, 'seven') # Вернет значение как и get но если нет значения создает ключ по параметру и дает ему значение None или дает ему как значение второй параметер

h.pop(7)# Вернет значение и удалит его

h.popitem() # Вернет случайное ключ и значение и удалит его

h.keys()
h.values()

for key,value in h.items():
    print(key, value)

print(h)
