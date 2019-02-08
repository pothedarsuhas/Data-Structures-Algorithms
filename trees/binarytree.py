class Node:
    def __init__(self, data):     #empty node
        self._data = data
        self._left = None
        self._right = None

    def get_data(self):
        return self._data

    def get_left_child(self):
        return self._left

    def get_right_child(self):
        return self._right

    def set_left_child(self, new_node):
        self._left = new_node

    def set_right_child(self, new_node):
        self._right = new_node

    def insert_left(self, data):
        node = Node(data)

        if self.get_left_child() is None:
            self.set_left_child(node)
        else:
            node._left = self.get_left_child()
            self.set_left_child(node)

    def insert_right(self, data):
        node = Node(data)

        if self.get_right_child() is None:
            self.set_right_child(node)
        else:
            node._right = self.get_right_child()
            self.set_right_child()



class binarytree:
    def __init__(self, data):       #creating root using node
        self._root = Node(data)

    def get_root(self):
        return self._root

    def _in_order(self, node):
        if node is None:
            return
        #print(node.get_data()) #preorder
        self._in_order(node.get_left_child())
        print(node.get_data()) #inorder
        self._in_order(node.get_right_child())
        #print(node.get_data()) #postorder

    def in_order(self):
        self._in_order(self.get_root())



t = binarytree(5)

t.get_root().insert_left(3)
t.get_root().insert_right(7)

left_child = t.get_root().get_left_child()
left_child.insert_left(2)
left_child.insert_right(4)

right_child = t.get_root().get_right_child()
right_child.insert_left(6)

print(t.in_order())

