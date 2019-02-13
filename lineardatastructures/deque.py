class emptydequeerror(Exception):
    pass

class deque():
    '''
    deque: hybrid datastructure
    operations:
    addfront(item), addrear(item)
    removefront(), removerear()
    isEmpty()
    size()

    '''
    def __init__(self):
        self._list = []

    def addfront(self, item):
        self._list.insert(0, item)

    def addrear(self, item):
        self._list.append(item)

    def isEmpty(self):
        return len(self._list) == 0

    def removefront(self):
        if self.isEmpty():
            raise emptydequeerror("trying to remove elements from an empty deque from front")
        self._list.pop(0)

    def removerear(self):
        if self.isEmpty():
            raise emptydequeerror("trying to remove elements from an empty deque from rear")
        self._list.pop()

    def size(self):
        return len(self._list)

if __name__ == "__main__":
    d = deque()
    d.addfront("hello")
    print(d.size())
    d.addrear("world")
    print(d.size())
    d.removefront()
    print(d.size())
    d.removerear()
    print(d.size())
    d.removerear()