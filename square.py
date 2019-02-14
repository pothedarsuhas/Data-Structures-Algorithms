import math
a = [(20, 10), (10, 20), ( 20, 20), (10, 10)]

def distance(a, b):
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return distance

def isSquare(a):
    a.sort()
    A = a[0]
    B = a[1]
    C = a[2]
    D = a[3]
    d12 = distance(A,B)
    d13 = distance(A,C)
    d14 = distance(A,D)

    d31 = distance(C,A)
    d34 = distance(C,D)
    d32 = distance(C,B)
    
    check1 = False
    check2 = False
    if d12 == d13 and d14 == math.sqrt(2) * d12:
        check1 =True
    if d31 == d34 and d32 == d14:
        check2 = True
    if check1 and check2:
        return True
    else:
        return False

print(isSquare(a))
