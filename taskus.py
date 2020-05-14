def copy_massiv(N):
    """
    копириует массив на вторую
    принимает len массива
    """
    A = [0]*N
    B = [0]*N
    for k in range(N):
        A[k] = int(input())
    for k in range(N):
        B[k] = A[k]
    B[0] = 56
    return("This is B:",  B)
# N=int(input())
# A = [0]*N
# B = [0]*N
# for k in range(N):
#     A[k] = int(input())
# for k in range(N):
#     B[k] = A[k]
# D = list(B)# Создает список на основе другого списка
# C = B # Перидает только ссылку так что это не дупликат и не изменяется
# B[0] = 56
# print("This is B:",  B)
# print(D)

def array_search(A:list, N:int, x:int):
    """Осуществляет поис числа х в массив А
    от 0 до N-1 индекса включительно.
    Возавращает индекс элеимента х в массив А.
    Или -1, если такого нет.
    Если в массиве несколько одинаковых элементов,
    равных х,  то тогда вернуть индекс первого.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    """Тест для функциий array_search
    """
    A1 = [1,2,3,4,5]
    m = array_search(A1, 5, 3)
    if m == 2:
        print("OK")
    else:
        print("NO")
    m = array_search(A1,5,6)
    if m == -1:
        print("OK")
    else:
        print("NO")
    A1[0] = 3
    m = array_search(A1,5,3)
    if m == 0:
        print("OK")
    else:
        print("NO")

def invert_array(A:list, N:int):
    """Оющение массива(поворот задом-наперед)
    в рамках индексов от 0 до N-1
    """
    for k in range(N//2):

        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array():
    A1 = [1,2,3,4,5]
    print(A1)
    invert_array(A1,5)
    print(5//2)
    print(5%2)
    print(A1)
    if A1 == [5,4,3,2,1]:
        print("Ok")
    else:
        print("NO")
    A2 = [0,0,0,0,0,0,0,10]
    invert_array(A2,8)
    print(A2)
    if A2 == [10,0,0,0,0,0,0,0]:
        print("OK")
    else:
        print("NO")

def index_step_left(A:list, N:int):
    """Сдвиг по индексу в ЛЕВО
    """
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp

def test_index_step_left():
    A1 = [0,1,2,3,4]
    index_step_left(A1,5)
    print(A1)
    if A1 == [1,2,3,4,0]:
        print("OK")
    else:
        print("NO")

def index_step_right(A:list, N:int):
    """Сдвиг по индексу в право
    """
    tmp = A[N-1]
    #range(start,stop,step)
    for k in range(N-2,-1,-1):
        A[k+1] = A[k]
    A[0] = tmp


def test_index_step_right():
    A1 = [1,2,3,4,5]
    index_step_right(A1,5)
    print(A1)
    if A1 == [5,1,2,3,4]:
        print("OK")
    else:
        print("NO")

def sieve_of_eratosthenes(N:int):
    """Решето Эратосфена алгоритм
    узнавание простового числа(число
    которое делятся только на саму себя)
    изночально берем 0 и 1 индексы состовными
    и считеаем что все числа True
    принимает N как конец индекса
    """
    N =int(input())
    A = [True]*N
    A[0] = A [1] = False

    for k in range(2, N):
        if A[k]:
            # Если A[k] True идет от 2k до N с шагом k миняя попути всех на False
            for m in range(2*k, N, k):
                A[m] = False
    for k in range(N):
        # Если A[k] True пичатоет про или сос
        # можно впихать внутрь print если тип boolean
        print(k, '-', "простое" if A[k] else "состовное")
