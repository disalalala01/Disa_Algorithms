"""
Декораторы
"""
from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result =  func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

def inputArg(arg):
    print(arg)
    def outer(func):
        def frapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return frapper
    return outer


# @timeit
def one(n):
    l = []
    for i in range(n):
        if i%2 == 0:
            l.append(i)
    return l

# @inputArg('name')
def two(n):
    l = [x for x in range(n) if x%2==0]
    return l

# l1 = timeit(one)
#
# l1 = timeit(one)(1000)

dis = inputArg('name')(two)(200)
print(dis)
