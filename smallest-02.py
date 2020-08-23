def find_two_smallest(L):
    L = 98, 12, 55, 123, 16
    if L[0] <= L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    for i in range(2, len(L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i
        return (min1, min2)
