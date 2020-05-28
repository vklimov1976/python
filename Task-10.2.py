'''
Упражнение 10.2
L = [-8, 8, 6.0, 5, 'string', -3.1]
Определить сумму чисел, входящих в список L. Подсказка: для определения типа объекта
можно воспользоваться сравнением вида type(-8) == int.
'''
L = [-8, 8, 6.0, 5, 'string', -3.1]

# first method

#for i in L:
#    if type(i) == str:
#        x = L.remove(i)
#print(sum(L))

# Second method
x = 0
for i in L:
    if type(i) == int or type(i) == float:
        x += i
print(x)