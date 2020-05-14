#--------------------------------РЕДАКЦИОННОЕ РАСТОЯНИЕ МЕЖДУ СТРОКАМИ ИЛИ РАСТОЯНИЕ ЛИВЕНШТЕЙНА ------------------------------

def levenstein(A, B):
    F = [[(i+j) if i*j==0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]

    for i in range(1,len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j]=F[i-1][j-1]
            else:
                F[i][j]=1+min(F[i-1][j], F[i][j-1], F[i-1][j-1])

    return F[len(A)][len(B)]

# A = "колокол"
# B = "молоко"
#
# s =levenstein(A,B)
# print(s)
#----------------------------ПРОВЕРКА РАВЕНСТВА СТРОК ------------------------

def equal_str(A, B):
    """ПРОВЕРЯЕТ НА
    РАВЕНСТВА СТРОКИ
    """
    if len(A)!=len(B):
        return False
    for i in range(len(A)):
        if A[i]!=B[i]:
            return False
    return True

# A = "salan"
# B = "salam"
# s = equal_str(A, B)
# print(s)

#------------------------------ПОЙСК ПОДСТРОКИ В СТРОКЕ ------------------------------

# s = "abacabadabacabafabacabadabacabadabacabafaba"
# sub = "dabac"
# print(s.count("dabac"))
def search_substring(s, sub):
    for i in range(0, len(s)-len(sub)):
        if equal_str(s[i:i+len(sub)], sub):
            print(i)

#------------------------------ПРЕФИКС ФУНКЦИЯ PI ОТ СТРОКИ------------------------------------
# СОБСТВЕННЫЙ СУФФИКС - СУФФИКС НЕ РАВНЫЙ САМОЙ СТРОКЕ
# PI - ДЛИНА МАКС СОБСТВЕННОГО СУФФИКСА КОТОРЫЙ ЯВЛЯЕТСЯ ПРЕФИКС

def knut_chris_moris_pratt(s):
    P = p[0 for i in ]          [FIXME] # Лек 13 последние 5 мин
    pass
