'''
Упражнение 9.4
L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
Определите наличие строки «привет» в списке. ЕСЛИ такая строка в списке присутствует,
ТО удалить ее из списка, ИНАЧЕ добавить строку в список.
Подсчитать, сколько раз в списке встречается число 4, ЕСЛИ больше одного раза, ТО
очистить список.
'''
pass
L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]

if 'привет' in L:
    L.remove('привет')
else:
    L.append('привет')
print (L)

M = L.count(4)
if M > 1:
    L.clear()
print (L)