from lineardatastructures.stack import stack

a = [1, 6, 4, 10, 2, 5]

def sm(a):
    min = a[0]
    a[0] = '_'
    for i in range(1, len(a)):
        temp = a[i]
        a[i] = min

        if temp < min:
            min = temp

    return a

def smln(a):
    

print(sm(a))

