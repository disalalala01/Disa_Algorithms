


#filter(func, iterable)


def has_o(string):
    return 'o' in string.lower()

l = ['One', 'TWO', 'three', '23Fkjsfo']

nl = list(filter(has_o, l))

newl = list(filter(lambda string: 'o' in string.lower(), l ))

dis = [ string for string in l if has_o(string) ]
print(dis)
