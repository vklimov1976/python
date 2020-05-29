'''
Упражнение 10.12
Дана матрица (см. упражнение 10.10). Вывести номер строки, содержащей
максимальное число одинаковых элементов.
'''
from random import randint
from collections import Counter

x, y = 5, 5


matrix = [ [randint(1,9) for i in range(x)] for i in range(y) ]

for i in matrix:
    print()
    for j in i:
        print(j, end=" ")
print("\n")