from stack import *

e = "*+ABC"
st = ""         #to convert prefix to infix, reverse the expression,  use this same program

for i in e:
    st = i + st
print(st)

s = stack()

operators = "+-*/"


for i in st:
    if i not in operators:
        s.push(i)
    elif i in operators:
        a = s.pop()
        b = s.pop()
        c = str(a)+str(i)+str(b)
        print(c)
        s.push(c)

print(s.pop())
