#------------------Лекция №7 Рекурсия----------------------------------
def matryoshka(n):
    if n==1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)

import graphics as gr

# window = gr.GraphWin("Game", 600, 600)
# alpha = 0.1
def fractal_rectangle(A, B, C, D, deep=10):
    if deep<1:
        return
    # gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    # gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    # gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    # вместо этого можно написать так перебирая его в цикле
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)

# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 100)
# x = int(input())

#-----------------------------------factorial-------------------------------------
from math import factorial
def f(n:int):
    """Факториал числа
    """
    assert n>=0, "Факториал неопределен" # Оператор assert генеририет ошибку если условие не правильное
    if n==0:
        return 1
    else:
        return f(n-1)*n#не считая n*n уходит в глубину и только возврашаясь доделовает работу

def test_f():
    t = factorial(14)# math factorial для проверки
    r = f(14)
    print("OK" if r==t else "NO")

#--------------------------------Алгоритм Евклида-------------------------------------------------
def gcd(a, b):
    """Определяет НОД(найбольший обший делитель)
    """
    if a==b:
        return a
    elif a>b:
        return gcd(a-b, b)
    else:     #a<b
        return gcd(a, b-a)

def gcd_2(a:int, b:int):
    """Определяет НОД(найбольший обший делитель)
    второй метод выполнения
    """
    # if b==0:
    #     return a
    # else:
    #     return gcd_2(b, a%b)
    return (a if b==0 else gcd_2(b, a%b))

def test_gcd():
    a = gcd(256, 80)
    b = 16
    print("OK" if a==b else "NO")
    print("2)")
    a = gcd_2(256, 80)
    print("OK" if a==b else "NO")

#----------------------------------Быстрое Возведение в степень(Рекурсивно)-----------------------------------------
def pow(a:float, n:int):
    """Быстрое Возведение в степень
    """
    if n==0:
        return 1
    elif n%2==1:
        return pow(a, n-1)*a#для не четных
    else:
        return pow(a**2,n//2)#Для четных чтобы было быстрее

def test_pow():
    a = pow(4, 3)
    print(pow(2, 1000))
    print("Ok" if a == 64 else "NO")

# ----------------------------------Ханойские Башний----------------------------------------------
