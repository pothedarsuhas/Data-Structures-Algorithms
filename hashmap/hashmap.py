from bs import *

class hashmap:

    def __init__(self):
        self.__capacity = 1000
        self._hashmap = [[]] * self.__capacity

    def calculate_hash(self, element):
        #print("index is ", element% self.__capacity)
        return element % self.__capacity

    def insert(self, element):
        index = self.calculate_hash(element)
        #print("index in insert is", index)
        if len(self._hashmap[index]) > 0:
            self._hashmap[index].append(element)
        else:
            self._hashmap.insert(index, [element])


    def search(self, element):
        index = self.calculate_hash(element)
        if len(self._hashmap[index]) > 1:
            return (index, BS(self._hashmap[index], 0, len(self._hashmap[index]) - 1, element)) \
                if BS(self._hashmap[index], 0, len(self._hashmap[index]) - 1, element) != -1 else -1
        else:
            return self._hashmap[index]
        # return self._hashmap[index]

    def expose(self):
        for i in self._hashmap:
            print(i)

h = hashmap()

testlist = []
for i in range(20001):
    testlist.append(i)

for i in testlist:
    h.insert(i)

print(h.search(20010))
