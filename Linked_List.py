
"""
Связанные списки | Linked List
"""
class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:

    def __init__(self):
        self.headval = None


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end='->')
            printval = printval.nextval
        print('None')

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
#  Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return None
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = NewNode


    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print('Упомянутый узел отсутствует')
            return None

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode



list = SLinkedList()
list.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
# Связываем первый node со вторым node
list.headval.nextval = e2

# Связываем второй с третим
e2.nextval = e3

list.AtBegining('Sun')
list.AtBegining('Disa')
list.AtEnd('Thu')
list.Inbetween(list.headval.nextval, "Fri")

list.listprint()
