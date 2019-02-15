class node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next_node(self, newnode):
        self.next = newnode

    def insert_node(self, data):
        newnode = node(data)
        if self.next is not None:
            self.next = self.get_next()
        self.set_next_node(newnode)

class cll:

    def __init__(self, data):
        self.root = node(data)

    def get_root(self):
        return self.root

    def make_circular(self):
        r = self.get_root()
        s = self.get_root()
        while r.get_next() is not None:
            r = r.get_next()
        r.next = s

    def circular_traverse(self):
        r =  self.get_root()
        count = 1
        while r.get_next() is not None and count == 1:
            if id(r.get_next()) == id(self.get_root()):
                count += 1
            print(r.get_data())
            r = r.get_next()

    def insert_n(self, data, n = -1):  # '1' for head, '-1' for end
        r = self.get_root()
        newnode = node(data)

        if n == -1:
            '''
            insert at the end
            '''
            while r.next is not None:
                if id(r.get_next()) == id(self.get_root()):
                    break
                r = r.next
            r.set_next_node(newnode)
            r.next.next = self.get_root()

        elif n == 1:
            newnode.next = r
            count = 1
            while r is not None and count == 1:
                r = r.next
                if id(r.get_next()) == id(self.get_root()):
                    count += 1
            r.next = newnode
            self.root = newnode

        else:
            round = 1
            count = 1
            while r is not None:
                if count + 1 == n:
                    break
                r = r.next
                count += 1
                if id(r.get_next()) == id(self.get_root()):
                    round += 1
            rend = r.next
            r.next = newnode
            newnode.next = rend



# c = cll(1)
#
# r = c.get_root()
#
# a = [2,3,4,5]
#
# for i in a:
#     r.insert_node(i)
#     r = r.get_next()
#
# c.make_circular()
#
# c.insert_n(6) # insert_n(data, position) for insertion at position head put position = 1, for tail put position = -1
#                   # for any node give position = n, by default this method inserts at end
#
#
# c.circular_traverse()
