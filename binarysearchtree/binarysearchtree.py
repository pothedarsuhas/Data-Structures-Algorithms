class node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data <= self.data:
            self.left = self.addtosubtree(self.left, data)
        else:
            self.right = self.addtosubtree(self.right, data)

    def addtosubtree(self, parent, data):
        if parent is None:
            return node(data)
        else:
            parent.add(data)
            return parent

class BST:

    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self.root.add(data)

    def _traverse(self, node):
        if node is None:
            return
        else:
            self._traverse(node.left)
            # if node.left is None and node.right is None: #leaves
            print(node.data)
            self._traverse(node.right)

    def traverse(self):
        self._traverse(self.root)

# l = [5,2,21,-4,3,19,25]
#
# b = BST()
#
# for i in l:
#     b.add(i)
#
# b.traverse()