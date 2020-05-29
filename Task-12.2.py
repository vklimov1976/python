'''
Упражнение 12.2
Напишите программу, которая для целочисленного списка из 1000 случайных
элементов определяет, сколько отрицательных элементов располагается между его
максимальным и минимальным элементами.
'''
from random import randint
 
lst = [randint(-100, 100) for _ in range(1000)]
mn, mx = lst.index(min(lst)), lst.index(max(lst))
if mn > mx:
    mn, mx = mx, mn
 
#print(len([i for i in lst[mn:mx] if i < 0]))
print(lst)