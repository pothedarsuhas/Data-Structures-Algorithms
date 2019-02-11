'''
GetLastElement();
RemoveLastElement();
AddElement()
GetMin()
'''

class ds:
    def __init__(self):
        self._list = []
        self._min = 1000000000000000

    def GetLastElement(self):
        return self._list[-1]

    def RemoveLastElement(self):            #this function is not complete
        if self._min == self.list[-1]:
            pass
        self._list.pop(-1)

    def AddElement(self, x):
        if x < self._min:
            self._min = x
        self._list.append(x)

    def GetMin(self):
        return self._min

d = ds()

d.AddElement(1)
d.AddElement(2)
d.AddElement(-100)
d.AddElement(-200)

print(d.GetLastElement())

print(d.GetMin())

d.RemoveLastElement()

print(d.GetLastElement())

print(d.GetMin())


