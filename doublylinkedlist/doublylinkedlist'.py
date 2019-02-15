class node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_next_node(self, newnode):
        if self.next is not None:
            self.next = self.get_next()
        self.next = newnode
        newnode.prev = self

    def set_prev_node(self, newnode):
        if self.prev is not None:
            self.prev = self.get_prev()
        self.prev = newnode
        newnode.next = self

    def insert_next_node(self, data):
        newnode = node(data)
        self.set_next_node(newnode)

    def insert_prev_node(self, data):
        newnode = node(data)
        self.set_prev_node(newnode)

class dll:

    def __init__(self, data):
        self.root = node(data)

    def get_root(self):
        return self.root

    def traversal(self):
        r = self.get_root()
        l = []

        while r.next is not None:
            l.append(r.get_data())
            r = r.get_next()

        r = self.get_root()
        while r.prev is not None:
            r = r.get_prev()
            l.insert(0,r.get_data())
        print(l)

# n = node(4)
# n.insert_next_node(5)
# n.insert_prev_node(3)
# print(n.get_next().get_data(), n.get_data(), n.get_prev().get_data())

# d = dll(4)
# r = d.get_root()
# right = [5,6,7,8]
# left = [1,2,3]
#
# while r.next is not None:
#     r = r.next
#
# for i in right:
#     r.insert_next_node(i)
#     r = r.next
#
# r = d.get_root()
#
# while r.prev is not None:
#     r = r.prev
#
# for i in left:
#     r.insert_prev_node(i)
#     r = r.prev
#
#
# print(d.get_root().get_prev().get_data(), d.get_root().get_data(), d.get_root().get_next().get_data())
# d.traversal()
#
