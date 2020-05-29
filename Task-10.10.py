'''
Упражнение 10.10
Создайте матрицу (список из вложенных списков) размера N x M (фиксируются в
программе), заполненную случайными целыми числами.
'''
print("=======================")
from random import randint
n = 3
m = 5
lst = [[randint(1,9) for i in range(n)] for i in range(m)]
for i in lst:
   print()
   for j in i:
       print(j, end=" ") 
print("\n=======================")