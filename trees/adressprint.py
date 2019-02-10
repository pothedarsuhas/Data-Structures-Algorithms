l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

d = []

for i in l:
    d.append(id(l[i]))

print(d)

if id(l[4]) in d:
    print(True)