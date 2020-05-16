'''
Упражнение 10.1
Найдите все значения функции y (x) = x 2 + 3 на интервале от 10 до 30 с шагом 2.
'''
def y(x):
    return x**2 + 3
#for x in range(10, 30+1, 2):
#    print(y(x))
#print([y(x) for x in range(10, 30+1, 2)])
print(*map(y, range(10, 30+1, 2)))