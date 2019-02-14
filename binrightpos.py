a = 18
a = bin(a)
a = a[2:]
# print(a)
s = ''
for i in a:
    s = i + s
# print(s)
for i in range(len(s)):
    if s[i] == '1':
        print(i+1)
        break