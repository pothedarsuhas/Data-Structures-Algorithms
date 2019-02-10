class emptystackerror(Exception):
    #raise a custom error
    pass

class stack:
    '''
    stack : LIFO data structure
    operations:
        push(item)
        pop()
        peek()
        isEmpty()
        size()
    '''

    def __init__(self):
        '''
        stack implementation using lists

        create an empty stack and to keep track of track create a variable
        '''

        self._list = []     #stack
        self._top = -1      #top

    def isEmpty(self):
        if self._top == -1:
            return True
        return False

    def push(self,item):
        self._list.append(item)
        self._top += 1

    def pop(self):
        if self.isEmpty():
            raise emptystackerror("Trying to pop an empty stack")
        self._list.pop()
        self._top -= 1

    def peek(self):
        if self.isEmpty():
            raise emptystackerror("Trying to peek an empty stack")
        return self._list[self._top]

    def size(self):
        return self._top + 1

    def expose(self):
        return (self._list)

# if __name__ == "__main__":
#     s = stack()
#     s.push("hello")
#     s.push("world")
#     s.pop()
#     print(s.peek())
#     s.pop()
#     print(s.size())


