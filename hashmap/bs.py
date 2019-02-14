def BS(l, low, high, x):
    # print(low, high)

    # print(mid)
    while low <= high:
        mid = (low + high) // 2

        if l[mid] == x:
            return mid
        elif x < l[mid]:
            return BS(l, low, mid - 1, x)
        elif x > l[mid]:
            high = len(l) -1
            return BS(l, mid + 1, high, x)

    return -1

# a= []
# for i in range(20000):
#     a.append(i)
#
# print(BS(a, 0, len(a)-1, 2223))