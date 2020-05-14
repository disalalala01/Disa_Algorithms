

"""
ЛЕКЦИЯ № 27

ДЕРЕВО ЭТО ГРАФ В КОТОРОМ НЕТ ЦИКЛОВ

- Двоичные деревья поиска.
- Асимптотика основных операций.
- Балансировка деревьев.
- Малый левый и правый повороты.
- Большой левый и правый повороты.


ДВОЙЧНОЕ ДЕРЕВО - КОРНЕВОЕ ДЕРЕВО, ГДЕ У ЛЮБОЙ ВЕРШИНЫ НЕ БОЛЕЕ ДВУХ ДОЧЕРНИХ



ДВОЙЧНОЕ ДЕРЕВО ПОЙСКА -  ЭТО СТРУКТУРА ДАННЫХ , ХРАНЯЩИЯ В ВЕРШИНАХ
ЭЛЕМЕНТЫ , СОДЕРЖАЩИЕ КЛЮЧ   KEY - ДОЛЖЕН ПРЕНАДЛЕЖАТЬ МНОЖЕСТВУ ПОТЕНЦИЯЛЬНЫХ
КЛЮЧЕЙ И ЭТО МНОЖЕСТВО ДОЛЖНО БЫТЬ УПОРЯДОЧЕННЫМ

вРЕМЯ ВЫПОЛНЕНИЕ ПОЙСКА ПРОПОРЦИОНАЛЬНО РАВНО ВЫСОТЕ ДЕРЕВО

ВЫСОТА  = K | КОЛИЧЕСТВО ЭЛЕМЕНТОВ (2**(K+1))-1

Дерево является сбалансированным, если для каждой вершины высота
ее левого и правого поддеревев  отличается не более чем на единицу

два вида балансировки Дерево

АВЛ - дерево
Красно-черное дерево(Кызыл кара агаш)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


    def insert(self, data):
        """Всавка внутрь дерева"""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(1)
root.insert(13)
root.insert(4)


root.PrintTree()
