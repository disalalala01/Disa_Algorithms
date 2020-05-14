

def upper(string):
    return string.upper()

l = ['one', 'two', 'three']

new_list = list(map(upper, l))# Функция пишется без скобок потому что ты его не вызываеш

print(new_list)

def map(func, iterable):
    for i in iterable:
        yield func(i)

new_l = list(map(lambda string: string.title(), l))
print(new_l)

nl = [ string.upper() for string in l ]

print(nl)
