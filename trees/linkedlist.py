class node:

    def __init__(self, data):
        self._data = data
        self._next = None

    def _get_data(self):
        return self._data

    def _get_next(self):
        return self._next

    def _set_next_node(self, newnode):
        self._next = newnode

    def _insert_node(self, data):
        newnode = node(data)

        if self._next is not None:
            self._next = self._get_next()
        self._set_next_node(newnode)

class linkedlist:

    def __init__(self, data):
        self._root = node(data)

    def _get_root(self):
        return self._root

    def _traverse(self, node):
        if node is None:
            return None
        else:
            print(node._get_data())
            self._traverse(node._get_next()) # if you place this above the above line the linked list is printed in the reverse order

    def traverse(self):
        return self._traverse(self._get_root())

    def search(self, data):
        count = 0
        r =self._get_root()
        while r._get_next() is not None:
            if r._get_data() == data:
                print(count)
            else:
                r = r._get_next()
                count += 1

    def insert_front(self, data):
        newnode = node(data)
        r = self._get_root()
        newnode._set_next_node(r)
        self._root = newnode

    def insert_end(self, data):
        newnode = node(data)
        r = self._get_root()
        while r._next is not None:
            r = r._next
        r._set_next_node(newnode)

    def insert_n(self, data , n):
        newnode = node(data)
        r = self._get_root()
        count = 1
        while r._next is not None :
            r = r._next
            count += 1
            if count == n:
                break
        rend = r._next
        r._set_next_node(newnode)
        r._next._next = rend

    def delete_front(self):
        r = self._get_root()
        self._root = r._next

    def delete_last(self):
        r = self._get_root()
        while r._next._next is not None:
            r = r._next
        r._next = None

    def delete_n(self, n):
        r = self._get_root()
        count = 1
        while r._next is not None:
            r = r._next
            count += 1
            if count == n-1:
                break
        if r._next is not None and r._next._next is not None:
            r._next = r._next._next

    def delete_list_data(self):
        r = self._get_root()
        while r._next is not None:
            r._data = None
            r = r._next
        r._data = None

    def length(self):
        count = 1
        r = self._get_root()
        while r._next is not None:
            count += 1
            r = r._next
        return count




# l = linkedlist(10)
#
# a = [20,30,40,50,60]
#
# l.insert_front(100)
#
# r = l._get_root()
#
# if r._get_next() is not None:
#     r = r._get_next()
#
# for i in a:
#
#     r._insert_node(i)
#     r = r._get_next()
#
#
# l.insert_end(8)
#
# l.insert_n(13, 5)
#
# l.delete_front()
# l.delete_last()
# l.delete_n(7)
#
# # l.delete_list_data()
#
# # del l
#
# # print(l.length())
#
# l.traverse()
