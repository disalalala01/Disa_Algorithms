

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
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
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()


    def inorderTraversal(self, root):
        """ Порядок обхода | Inorder traversal
        Left -> Root -> Right
        """
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


    def preorderTraversal(self, root):
        """Предварительный заказ обхода| Preorder Traversal
        Root -> Left ->Right
        """
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res


    def postorderTraversal(self, root):
        """Обход после заказа | Postorder Traversal
        Left ->Right -> Root
        """
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
