'''
Упражнение 10.3
Дан список числовых значений, насчитывающий N элементов. Поменяйте местами
первую и вторую половины списка.
'''
a = [4,6,7,8,1,5,3]
b = len(a) // 2
print(a[b:] + a[:b])

