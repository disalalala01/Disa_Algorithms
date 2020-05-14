#------------------------------------БИНАРНЫЙ ПОЙСК В МАССИВЕ------------------------------------------
# ДЛЯ БИНАРНОГО ПОЙСКА МАССИВ ДОЛЖЕН БЫТЬ ОТСОРТИРОВАННЫМ
def left_bound(A:list, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (left + right)//2
        if A[middle]<key:
            left  = middle
        else:
            right = middle
    return left

# A= [5,4,3,2,1]
# B =[1,2,3,4,7]
# s= left_bound(A, 2)
print(s)
def right_bound(A:list, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (left + right)//2
        if A[middle]<=key:
            left  = middle
        else:
            right = middle
    return right
# d = right_bound(B)
# print(d)

#-------------------------------------------ДИНАМИЧЕСКОЕ  ПРОГРАМИРОВАНИЕ------------------------------
#----------ФИБОНАЧЧИ
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)


def fib_2(n):
    fib = [0,1]+[0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]

#----------------------------КУЗНЕЧИК-------------------
#------------ЗАПРЕТ ДЛЯ НЕКОТОРЫХ КЛЕТОК -----------------
def count_tragictoies_num(n:int, allowed:list):
    """Сколько раз может допрыгнуть кузнечик
    если он может 1.2.3 клеток и нелзя
    прыгать на некоторые за сколько ходов допрыгнет
    кузнечик
    """
    # K = [0,1]+[0]*n ПРИ ОБЫЧНЫХ СЛУЧАЯХ БЕЗ ЗАПРЕТОВ
    # for i in range(2, n+1):
    #     K[i] = K[i-2]+K[i-1]
    #    return K[N]
    K = [0,1,int(allowed[2])]+[0]*(n-3)#ДАЕШ ЛИСТ ИЗ КЛЕТОК КОТОРЫХ ПОСИШАТЬ НЕЛЬЗЯ ОН ПРОВЕРЯЕТ КЛЕТКУ ИФОМ В ФОРИКЕ И ЕБАШИТ ОСТАЛЬНЫЕ
    for i in range(3, n+1):
        if allowed[i]:
            K[i]=K[i-1]+K[i-2]+K[i-3]


# ЗА ПОСИШЕНИЕ КЛЕТКИ ДАЕТСЯ ОПРЕДЕЛЕННЫЙ ПРАЙС
def count_min_cost(N:int, price:list):
    """ЗА САМУЮ МЕНЬШУЮ СТОЙМОСТЬ
    ПОПАСТЬ ДО N
    """
    C = [float("-inf"), price[1], price[1]+price[2]]+[0]*(n-2) #float -INF ОЗНОЧАЕТ -БЕСКОНЕЧНОСТЬ c ПЛАВУЮЩЕЙ ТОЧКОЙ МЕНЬШЕ ЛЮБОГО ЧИСЛА
    for i in range(3, N+1):
        C[i] = price[i]+min(C[i-1],C[i-2])

    return C[N]

#---------------------------------------------------ДВУМЕРНЫЕ МАССИВЫ -----------------------------------------------
"""
A = [ [0]*M for i in range(N)]# ПРАВИЛЬНОЕ ГЕНЕРАЦИЯ ДВУМЕРНОГО МАССИВА
A[0] == A[1] # TRUE
A[o] is A[1] # FASLE ОПЕРАТОР IS СРАВНИВАЕТ НЕ ПО ИМЕНИ А ПО ССЫЛКАМ ДВУХ ОБЕКТОВ
"""
