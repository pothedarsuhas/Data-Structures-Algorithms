#using min heaps


class emptyheaperror(Exception):
    pass

class minheap:
    def __init__(self):
        self._list = [0] #initialising a list with index 1
        self._size = 0

    def _size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def find_minimum(selfs):
        if self.isEmpty():
            raise emptyheaperror("You are trying to find minimum from an empty heap")
        return self._list[1]

    def insert(self, key):
        self._list.append(key)
        self._size += 1
        self._perc_up(self._size)

    def delete_minimum(self):
        if self.isEmpty():
            raise emptyheaperror("You are trying to delete minimum from an empty  heap")
        minimum = self._list[1]
        self._list[1] = self._list.pop()
        self._size -= 1
        self._perc_down(1)

        return minimum

    def _perc_up(self, pos):
        while pos // 2 > 0:
            if self._list[pos] > self._list[pos // 2]:
                (self._list[pos], self._list[pos // 2]) = (self._list[pos // 2], self._list[pos])
            pos = pos // 2

    def _perc_down(self, pos):
        pass




    def __repr__(self):
        return str(self._list)