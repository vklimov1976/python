print("\n================Вложеные циклы=============================")
outer = [1,2,3,4] # внешний цикл
inner = [5,6,7,8] # вложеный (внутренний) цикл
for i in outer:
    for j in inner:
        print("i=", i, "j=", j)

#
print("\n=================Пример с одним циклом for==================")
lst = [ [1,2,3],
        [4,5,6] ]
for i in lst:
    print(i)
print("\n============================================================")
print("Если мы хотим добраться до элементов вложенных списков, \nто придется использовать вложенный цикл for:")
print("============================================================")
for i in lst: # цикл по элементам внешнего писка
    print()
    for j in i: # цикл по элементам элементов внешнего писка
        print(j, end=" ")
print("\n============================================================")