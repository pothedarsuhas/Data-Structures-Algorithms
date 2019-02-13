# not complete, doesnt work when the minimum is removed from this datastructure

'''
GetLastElement();
RemoveLastElement();
AddElement()
GetMin()
'''

class ds:
    def __init__(self):
        self._list = []
        self._min = None

    def isEmpty(self):
        return len(self._list) == 0

    def GetLastElement(self):
        return self._list[-1]

    def RemoveLastElement(self):
        if self.isEmpty():
            print("You are trying to remove an element from empty datastructure")
        else:
            t = self._list.pop(-1)
            if t < self._min:
                self.min = 2 * self._min - t

    def AddElement(self, x):
        if self.isEmpty():
            self._min = x
        if x < self._min:
            self._min = x
        self._list.append(x)

    def GetMin(self):
        return self._min

d = ds()

d.AddElement(1)
d.AddElement(2)
d.AddElement(-100)
d.AddElement(-300)

print(d.GetLastElement())

print(d.GetMin())

d.RemoveLastElement()

print(d.GetLastElement())

print(d.GetMin())


