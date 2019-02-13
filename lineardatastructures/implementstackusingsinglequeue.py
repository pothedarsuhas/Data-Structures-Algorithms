from queue import *

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

sz = q.size()
count = 0

while sz > 0:
    x = q.dequeue()
    q.enqueue(x)
    count += 1
    if q.size() == 1:
        print(q.dequeue())
        sz -= 1
    if count == sz - 1:
        print(q.dequeue())
        count = 0
        sz -= 1




