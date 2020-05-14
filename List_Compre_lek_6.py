#лекция №6 работа с листом
"""
A = []
x = int(input())
A.append(x)# добавляет
n = len(A)
A.pop()# удаляет с конца(может возврашять остаток, а может продолжать дальше)
# ---------------------List Comprehensions---------------------------------------\
A = [x**2 for i in range(10)]#Это эквивалентно этому
#-----------------\\\\\\-----------------------
A = []
x = int(input())
for i in range(10):
    A.append(x**2)
"""
#---------------------------------------------------------------\

def square_all_even(A:list):
    """Возавращает второй лист где
    все элементы четные и в квадрате
    A = [1,2,4,14,25,64,16,76,23,5,9]
    B = []
    for x in A:
        if x%2==0:
            B.append(x**2)
    Вместо этого можно так
    """
    A = [i**2 for i in A if i%2 == 0]
    return A

def test_square_all_even():
    B = [1,2,4,14,25,64,16,76,23,5,9]
    m = square_all_even(B)
    print(m)
    if m == [4, 16, 196, 4096, 256, 5776]:
        print("OK")
    else:
        print("NO")



#------------------------------------------------------Sort----------------------------------------

def insert_sort(A:list):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A
B = [5, 6, 8, 1, 2, 4, 3, 7 ]

x = insert_sort(B)
print(x)

def choise_sort(A:list):
    N= len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A
A = [5, 6, 8, 1, 2, 4, 3, 7 ]
s = choise_sort(B)
print(s)

def bubble_sort(A:list):
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k]>A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

    return A

C = [8, 7,4, 3,-5, 2 ,1, 6]
e = bubble_sort(C)
print(e)
