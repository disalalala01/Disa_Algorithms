
#------------------------ПРОВЕРКА ПОСЛЕДОВАТЕЛЬНОСТИ СКОБОЧНОЙ ПОСЛЕДОВАТЕЛЬНОСТИ----------------------------

# А="" это корректно
# B = A это корректно
# C = AB это корректно
# "(((())))()((()))" это корректно
# "())(()" это не корректно
#  "[(])" это не корректно

import A_stack

def is_braces_sequence_correct(s:str):
    """
    ПРОВЕРЯЕТ КОРРЕКТНОСТЬ СКОБОЧНОЙ ПОСЛЕДОВАТЕЛЬНОСТИ
    ИЗ КРУГЛЫХ И КВАДРАТНЫХ СКОБОК [] ()

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("([]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    """
    for brace in s:
        if brace not in "() []":
            continue
        if brace in "([":
            A_stack.push(brace)
        else:
            assert brace in ")]" , "Ожидалось закрывающая скаобка: " + str(brace)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([", "Ожидалось открывающая скобка: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return A_stack.is_empty()



# if __name__ == "__main__":
#     from doctest import testmod
#     testmod(verbose=True)

#---------------------------------ОБРАТНАЯ ПОЛЬСКАЯ НОТАЦИЯ-----------------
#-------АЛГОРИТМ ВЫЧЕСЛЕНИЯ ВЫРАЖЕНИЙ В ПОСТФИКСНОЙ НОТАЦИЙ -------------------

#    [5,2,'+'] >>>> 5+2          (2+7)*5>>>>>[2, 7, 5, *, +]

[ADDME]
[FIXME]
