'''
Упражнение 12.3
Найти элемент, наиболее близкий к среднему значению всех элементов списка.
'''
from random import randint

def funL(L):
    y = L[:]
    w = sum(L) / len(L)     # среднее значение
    for i, k in enumerate(L):
        L[i] = abs(k - w)   # создаем массив из чисел массива за минусом их среднего арифметического. тут выдается ошибка IndexError: list index out of range
        v = min(L)          # находим минимальную дельту меду элементом и средним арифметическим
        return y[L.index(v)]

p = [randint(1, 9) for i in range(5)]
print(funL(p))