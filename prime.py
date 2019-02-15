import math

def prime(n):
    count = 0
    for i in range(2,(int(math.sqrt(n)))):
        if n % i == 0:
            print(n, '%', i,'=', n%i)
            count += 1

    if count == 0:
        return True
    else:
        return False

print(prime(13))

