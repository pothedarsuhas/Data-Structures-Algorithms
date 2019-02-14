a = [0,0,0,1,1,2,2,2,2,2,3,4,4,4,4,4,4,4,5,5,6,6,6,6,7,8,8,8,8,8,8,8,8,8,8,8]

freq = {}

b = []

for i in a:
    if i not in b:
        b.append(i)

for i in b:
    freq[i] = a.count(i)

print(freq)


