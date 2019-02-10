from lineardatastructures.stack import *

from trees.linkedlist import *

l = linkedlist('b')

a = ['b', 'b']

r = l._get_root()

if r._get_next() is not None:
    r = r._get_next()

for i in a:
    r._insert_node(i)
    r = r._get_next()

l.traverse()

s = stack()

r = l._get_root()

while r._get_next() is not None:
    s.push(r._data)
    r = r._next
s.push(r._data)

r = l._get_root()

s.expose()

while r._get_next() is not None:
    if r._get_data() == s.peek():
        s.pop()
        s.expose()
    r = r._next
if r._data == s.peek():
    s.pop()
    s.expose()


if s.isEmpty():
    print(True)
else:
    print(False)