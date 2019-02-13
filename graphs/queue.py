class emptyqueueerror(Exception):

    pass

class queue():

    '''
    queue: FIFO data structure
    operations:
    enqueue()
    dequeue()
    size()
    isEmpty()

    considering the rear end as the non zero index extreme, and front end at zero index
    '''

    def __init__(self):
        self._list = []

    def enqueue(self, item):
        self._list.append(item)

    def size(self):
        return len(self._list)

    def isEmpty(self):
        return len(self._list) == 0

    def dequeue(self):
        if self.isEmpty():
            raise emptyqueueerror("Trying to dequeue an empty queue")
        else:
            return self._list.pop(0)

# if __name__ == "__main__":
#     q = queue()
#
#     q.enqueue("hello")
#     print(q.size())
#     q.enqueue("world")
#     print(q.size())
#     q.dequeue()
#     print(q.size())
#     print(q.isEmpty())
#     q.dequeue()
#     print(q.size())
#     print(q.isEmpty())
#     q.dequeue()