

# -------------------------------------------Генерация всех перестановок--------------------------------------------------------

def generate_number(N:int, M:int, prifix=None):

    prifix = prifix or []
    if M==0:
        print(prifix)
        return
    for digit in range(N):
        prifix.append(digit)
        generate_number(N, M-1, prifix)
        prifix.pop()#   Убрать с конца


def gen_bin(M:int, prefix =""):
    if M == 0:
        print(prefix)
    else:
        for zerone in "0","1":
            gen_bin(M-1, prefix+zerone)
        # gen_bin(M-1, prefix +"0")
        # gen_bin(M-1, prefix +"1")

def find(x:int, A:list):
    """Ишет число внутри списка
    """
    flag = False
    for number in A:
        if x == number:
            flag = True
            break
    return flag




def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
    с префиксом
    """
    M = N if M == -1 else M # По умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep=' ,')# * встраевает список внутрь параметров списка
        return
    for number in range(1, N+1):
        # if number was in prefix: # Fixme
        #     continue # Если True пропускает
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()



#---------------------------------------------------------------Рекурентное сортировка ---------------------------------------

#--------------------------------------------------------Быстрое Сортировка ТОни Хоара( QUICK SORT) -----------------------------------------------------------
                                                #--------------ВыПОЛНЯЕТСЯ НА ПРЯМОМ ХОДУ РЕКУРСИИ
                                                # -------------ВЫПОЛНЯЕТСЯ БЕЗ ДОПОЛНИТЕЛЬНОЙ ПАМЯТИ
                                                #-----------АЛГОРИТМ (РАЗДЕЛЯЙ И ВЛАСТВУЙ)

def hoar_sort(A:list):
    if len(A)<=1:
        return None
    L=[]
    M=[]
    R=[]
    barrier = A[0]
    for x in A:
        if x<barrier:
            L.append(x)
        elif x==barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k=0
    for x in L+M+R:
        A[k] = x
        k+=1
    return A
A = [4,2,5,1,3,7,8,6,9,10]
s = hoar_sort(A)
print(s)

def check_sorted(A:list, ascending = True):
    """Проверка отсортированности за O(len(A))
    """
    s = 2*int(ascending)-1
    flag = True
    for i in range(0, N-1):
        if s*A[i]>s*A[i+1]:
            flag = False
            break
    return flag


#-----------------------------------------------------------Сортировка Слиянием--------------------------------------------------------------------
                                                #------------ВЫПОЛНЯЕТ НА ОБРАТНОМ ХОДУ РЕКУРСИИ
                                                #------------ НУЖНА ДОПОЛНИТЕЛЬНАЯ ПАМЯТЬ



#  АЛГОРИТМ СЛИЯНИЯ НЕ СОРТИРОВКА ПРОСТО СЛИЯНИЕ ДВУ СПИСКОЫ
def merge(A:list, B:list):
    C = [0]*(len(A)+ len(B))
    i = 0
    k = 0
    n = 0
    while i<len(A) and k < len(B):
        if A[i]<=B[k]:
            C[n]=A[i]
            i+=1
            n+=1
        else:
            C[n]= B[k]
            k+=1
            n+=1
    while i < len(A):
        C[n]= A[i]
        i+=1
        n+=1
    while k<len(B):
        C[n]=B[k]
        k+=1
        n+=1
    return C



#   АЛГОРИТМ СОРТИРОВКИ СЛИЯНИЕМ

def merge_sort(A:list):
    if len(A)<=1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0,middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i]=C[i]
    return A
