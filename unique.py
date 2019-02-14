def unique(a):
    freq = {}
    b = []
    for i in a:
        if i not in b:
            b.append(i)

    for i in b:
        freq[i] = a.count(i)
    max = 0
    for i in freq.values():
        if i > max:
            max = i
    return max <= 1

for i in range(20):
    if unique(str(i)):
        print(i)

